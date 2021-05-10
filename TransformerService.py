# By Jacob Vilevac
# Transformer Service that converts addresses into google maps urls.
import tkinter as tk

testAddy = ["Target Plaza1000 Nicollet MallMinneapolis, Minnesota, U.S.","-33.712206,150.311941","San Jose, California, United States37°20′07″N 121°52′53″W﻿ / ﻿37.3353°N 121.8813°W﻿ / 37.3353; -121.8813Coordinates: 37°20′07″N 121°52′53″W﻿ / ﻿37.3353°N 121.8813°W﻿ / 37.3353; -121.8813"]

def main():
    testConvert()
    
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


def guiButtonPress():
    textIn = text.get("1.0", "end-1c")
    textIn = textIn.splitlines()
    #text.delete("1.0", "end-1c")
    textOutArray = convertAddresses(textIn)
    textOut = "\n"
    for addr in textOutArray:
        textOut += (addr + "\n")

    label2.pack()
    text2.pack(fill=tk.BOTH, expand=True)
    text2.delete("1.0", "end-1c")
    text2.insert(tk.END, textOut)

main()

# GUI
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


label2 = tk.Label(
    text="Output Google Maps Links",
    foreground="black",  # Set the text color to white (fg shorthand)
    #background="white"  # Set the background color to black (bg shorthand)
)
text2 = tk.Text(
    fg="black", 
    bg="#fefefe",
    width=50
)

button = tk.Button(
    text="Transform",
    command=guiButtonPress,
    width=10,
    height=2,
    bg="#fefefe",
    fg="black",
)
label.pack()
text.pack(fill=tk.BOTH, expand=True)
button.pack()

window.mainloop()