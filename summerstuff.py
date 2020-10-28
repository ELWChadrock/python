from tkinter import *
import tkinter as tk
import webbrowser

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Summer Sale!')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def custompage():
    customentry = entry1.get()
    f = open("summer.html", "w")
    htmlformat=opentags+customentry+closetags
    f.write(htmlformat)
    f.close()
    webbrowser.open_new_tab("summer.html")

button1 = tk.Button(text='Submit your answer!', bg='brown', fg='white', font=('helvetica', 9, 'bold'), command=custompage)
canvas1.create_window(200, 180, window=button1)

message = """<html> 
     <body> 
	<h1>
          Stay tuned for our amazing summer sale! 
       </h1>
     </body> 
</html>"""
opentags="<html>\n<body>\n<h1>"
closetags="</h1>\n</body>\n</html>"

##f.write(message)
##def custompage():
##    customentry = entry1.get()
##    f = open("summer.html", "w")
##    htmlformat=opentags+customentry+closetags
##    f.write(htmlformat)
##    f.close()
##    webbrowser.open_new_tab("summer.html")

##url = 'file:///C:/Users/Zeroh/Desktop/Python/website/summer.html'
##webbrowser.open_new_tab(url)

