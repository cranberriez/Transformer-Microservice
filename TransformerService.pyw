# By Jacob Vilevac
# Transformer Service that converts addresses into google maps urls.
import tkinter as tk
from tkinter import filedialog
import csv

# Global Data
employerData = []
global transformed
transformed = False

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

def guiClearTable():
    for cell in data_frame.winfo_children():
        cell.destroy()

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

def guiOpen(filename):
    global transformed
    global employerData
    if filename:
        file_path = filename
    else:
        file_path = filedialog.askopenfilename()

    if not file_path:
        return
    if not file_path.endswith(".csv"):
        tk.messagebox.showwarning(title="Invalid Filetype", message="Only .csv files can be opened with this transformer service!")
        return

    guiClearTable()

    with open(file_path, newline='\n') as csvfile:
        employerData = []
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            for col in row:
                if col.find("N/A") != -1 or col.find("°") != -1:
                    col = "N/A"
            employerData.append(row)
        
        for col in employerData[0]:
            if col == "Google URL":
                transformed = True

        guiCreateDataTable(employerData)

    window.title(f"Address Transformer Service - {file_path}")

def guiTransform():
    global transformed

    if not employerData:
        return
    if transformed:
        return

    employerData[0].append("Google URL")

    for row in employerData[1:]:
        row.append((convertToUrl(row[3])))

    guiClearTable()

    guiCreateDataTable(employerData)
    transformed = True

def guiSaveAs(filename):
    fileExtentions = [("Comma Seperated Values", '*.csv')]
    if filename:
        file_path = filename
    else:
        file_path = filedialog.asksaveasfile(mode='w', filetypes = fileExtentions, defaultextension = fileExtentions)
    if file_path is None:
        return
    with open('innovators.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in employerData:
            writer.writerow(row)

# GUI
window = tk.Tk()
useGUI = True

def createGUI():
    window.title("Employer Transformer Service")

    window.rowconfigure(0, minsize=500, weight=1)
    window.columnconfigure(1, minsize=500, weight=1)

    global data_frame
    data_frame = tk.Frame(window)
    global fr_buttons
    fr_buttons = tk.Frame(window, bg="#686868", pady=5)

    btn_open = tk.Button(fr_buttons, text="Open .csv", command= lambda: guiOpen(0))
    btn_transform = tk.Button(fr_buttons, text="Transform", command= lambda: guiTransform())
    btn_save = tk.Button(fr_buttons, text="Save As", command= lambda: guiSaveAs(0))

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_transform.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    data_frame.grid(row=0, column=1, sticky="nsew")

    window.mainloop()

def main():
    if (useGUI):
        createGUI()

main()