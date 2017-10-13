# -*- coding: utf-8 -*-
import tkinter as tk

root  = tk.Tk()

root.title("Simple gui")
root.geometry("200x200")


app = tk.Frame(root)
label = tk.Label(app, text= "this is a lable")

button1 = tk.Button(app,text= "Button1")
button2 = tk.Button(app,text="Button2")

app.grid()
label.grid()
button1.grid()
button2.grid()

root.mainloop()

