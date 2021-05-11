# By Jacob Vilevac
# Transformer Service that converts addresses into google maps urls.
import tkinter as tk
from tkinter import filedialog

# Global Data
employerData = 0
transformed = False

def testConvert():
    converted = convertAddresses(testAddy)
    for addr in converted:
        print(addr)

def convertToUrl(addr):
    # Encoding Rules
    #   %7C = |
    #   %20 = space
    #   %2C = ,

    if addr.find("N/A") != -1 or addr.find("°") != -1:
        return "N/A"
    else:
        output = addr.replace('|', '%7C').replace(' ', '%20').replace(',', '%2C')
        output = "https://www.google.com/maps/search/?api=1&query=" + output
        return output

def convertFromCSV(csv):
    csv = csv.split("\n")
    csv.pop()
    i = 0
    for item in csv:
        csv[i] = item.replace("\"","").split(",",3)
        i = i + 1
    
    return csv

def convertToCSV(data):
    outputCSV = ""

    for i in data:
        for j in i:
            val = j
            try:
                val = int(val)
                outputCSV += (j + ",")
            except ValueError:
                outputCSV += ("\"" + j + "\"" + ",")
        outputCSV += "\n"

    return outputCSV

def guiCreateDataTable(employerData):
    for i in range(len(employerData)):
        for j in range(len(employerData[i])):
            cell = tk.Frame(
                master = data_frame,
                relief = tk.RAISED,
                borderwidth = 1)
            cell.grid(row = i, column = j, sticky="ew")
            cellText = employerData[i][j]
            if cellText.find("N/A") != -1 or cellText.find("°") != -1:
                cellText = "N/A"
            label = tk.Label(master = cell, text = cellText, anchor="w", justify="left", padx=3, pady=2)
            label.pack(fill="both")

def guiOpen():
    global transformed
    transformed = False

    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    if not file_path.endswith(".csv"):
        return

    for cell in data_frame.winfo_children():
        cell.destroy()

    with open(file_path, "r") as input_file:
        text = input_file.read()
        global employerData 
        employerData = convertFromCSV(text)
        guiCreateDataTable(employerData)

    window.title(f"Employer Transformer Service - {file_path}")

def guiTransform():
    global transformed
    if not employerData:
        return
    if transformed:
        return

    employerData[0].append("Google URL")

    for row in employerData[1:]:
        row.append((convertToUrl(row[3])))

    for cell in data_frame.winfo_children():
        cell.destroy()

    guiCreateDataTable(employerData)
    transformed = True

def guiSaveAs():
    fileExtentions = [("Comma Seperated Values", '*.csv')]
    file = filedialog.asksaveasfile(mode='w', filetypes = fileExtentions, defaultextension = fileExtentions)
    if file is None:
        return
    dataToSave = convertToCSV(employerData)
    file.write(dataToSave)
    file.close()

# GUI
window = tk.Tk()

window.title("Employer Transformer Service")

window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

data_frame = tk.Frame(window)
fr_buttons = tk.Frame(window, bg="#686868", pady=5)

btn_open = tk.Button(fr_buttons, text="Open .csv", command=guiOpen)
btn_transform = tk.Button(fr_buttons, text="Transform", command=guiTransform)
btn_save = tk.Button(fr_buttons, text="Save As", command=guiSaveAs)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_transform.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
data_frame.grid(row=0, column=1, sticky="nsew")

window.mainloop()