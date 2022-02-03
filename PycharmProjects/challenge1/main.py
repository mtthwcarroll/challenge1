import tkinter as tk
from tkinter import StringVar
import csv
import re

global searchVar
global txtList
global lblSearch

# GUI for the program
class gui:
    # Initialize
    def __init__(self):
        global searchVar
        global txtList
        global lblSearch

        self.wn = tk.Tk()
        self.wn.geometry("720x480")

        lblSearch = tk.Label(self.wn, text="Search by prefix. Leave empty for all counties")
        lblSearch.grid(row=1, column=1, columnspan=2)

        searchVar = StringVar()
        txtBoxSearch = tk.Entry(self.wn, textvariable=searchVar)
        txtBoxSearch.grid(row=2, column=1, padx=5, pady=5)

        btnSearch = tk.Button(self.wn, text="Search", width=10)
        btnSearch.grid(row=2, column=2, sticky=tk.W, pady=5, padx=5)
        btnSearch.config(command=search)

        txtList = tk.Listbox(self.wn, width=30, height=20)
        txtList.grid(row=3, column=1, pady=5, padx=5, columnspan=2)

        btnExit = tk.Button(self.wn, text="Exit", width=10)
        btnExit.grid(row=4, column=1, columnspan=2)
        btnExit.config(command=exit)

    def exit(self):
        self.wn.destroy()

    # Start the GUI
    def start(self):
        self.wn.mainloop()

def readCounties(filename):
    dict = {}
    with open(filename) as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            dict[row[2]] = row[0] + ", " + row[1]
    return dict

def search(event=None):
    global searchVar
    global txtList
    global lblSearch

    valid = inputValidation(searchVar.get())

    lblSearch.config(text="Search by prefix. Leave empty for all counties")

    if valid:
        txtList.delete(0, tk.END)
        dictionary = readCounties("MontanaCounties.csv")
        if searchVar.get() == '':
            index = 0
            for key in dictionary:
                txtList.insert(index, key + ", " + dictionary[key])
        else:
            index = 0
            for key in dictionary:
                if key == searchVar.get():
                    txtList.insert(index, key + ", " + dictionary[key])
    else:
        lblSearch.config(text="Please enter a valid input.")

def inputValidation(string):
    if string == '':
        return True
    else:
        expr = re.sub(r'[0-9]', '', string)
        if expr != '':
            return False
        else:
            return True

if __name__ == "__main__":
    gui = gui()
    gui.start()
