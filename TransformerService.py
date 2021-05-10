# By Jacob Vilevac
# Transformer Service that converts addresses into google maps urls.
import tkinter as tk

testAddy = ["310 SW Weatherford Place", "300 SW 26th Street","2501 SW Jefferson Way","2520 SW Campus Way","3051 SW Campus Way","3550 SW Jefferson Way","661 SW 26th Street"]

def main():
    createGui()
    
def testConvert():
    converted = convertAddresses(testAddy)
    for addr in converted:
        print(addr)

def convertAddresses(array):
    output = []

    for addr in array:
        output.append(convertToUrl(addr))

    return output

def convertToUrl(addr):
    output = addr.replace('|', '%7C').replace(' ', '%20').replace(',', '%2C')
    output = "https://www.google.com/maps/search/?api=1&query=" + output
    return output

def createGui():
    window = tk.Tk()
    label = tk.Label(
        text="Please input addresses seperated by a new line.",
        foreground="black",  # Set the text color to white (fg shorthand)
        #background="white"  # Set the background color to black (bg shorthand)
    )

    text = tk.Text(
        fg="black", 
        bg="#fefefe",
        width=50
    )

    button = tk.Button(
        text="Submit",
        command=testConvert,
        width=10,
        height=2,
        bg="#fefefe",
        fg="black",
    )
    label.pack()
    text.pack(fill=tk.BOTH, expand=True)
    button.pack()

    #text.get("1.0", tk.END) #gets all text in textbox


    window.mainloop()

main()

# Encoding Rules
#   %7C = |
#   %20 = space
#   %2C = ,