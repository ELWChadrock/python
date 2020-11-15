import shutil
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os


def transfer1():
    source = tkinter.filedialog.askdirectory()
    entry1.insert(0, source)

def transfer2():
    destination = tkinter.filedialog.askdirectory()
    entry2.insert(0, destination)

def transfer3():
    v = entry1.get()
    n = entry2.get()
    files = os.listdir(v)
    for file in files:
        if file.endswith(".txt"):
            os.path.abspath("/Users/Zeroh/Desktop/Python/filetransfer1/")
            modification_time = os.path.getmtime()

root = Tk()

button1 = tk.Button(text='From', bg='brown', fg='white', font=('helvetica', 9, 'bold'), command=lambda:transfer1())
button1.grid(column=1, row=1)


button2 = tk.Button(text='New Destination', bg='brown', fg='white', font=('helvetica', 9, 'bold'), command=lambda:transfer2())
button2.grid(column=1, row=2)


button3 = tk.Button(text='Transfer', bg='brown', fg='white', font=('helvetica', 9, 'bold'), command=lambda:transfer3())
button3.grid(column=1, row=3)

entry1 = tk.Entry (root)
entry1.grid(column=2, row=1)

entry2 = tk.Entry (root)
entry2.grid(column=2, row=2)
            
            
            
    
