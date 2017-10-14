# -*- coding: utf-8 -*-
from tkinter import *

class Application (Frame):
    def __init__(self,master):
        """Initializes the frame"""
        Frame.__init__(self,master)
        self.buttonClicks = 0
        self.create_widgets()
        self.grid()
        
        
    def create_widgets(self):
        """Create button that counts number of clicks"""
        self.label = Label(self, text= "this is a lable" + str(self.buttonClicks))
        self.label.grid(row=0,sticky=W,padx=10,pady=20)
        
        self.entrs = Entry(self,width=10)
        self.entrs.grid(row = 1,column = 0, padx = 20, sticky = W)
        
        self.button1 = Button(self,text="total clicks " + str(self.buttonClicks))
        self.button1.bind("<Button-1>",self.update_count)
        self.button1.grid(column = 0,row = 2,sticky = W)
        
        self.radio1 = Radiobutton(self,text="Good",value=1)
        self.radio1.grid(column = 0,row = 3, sticky = W)
        self.radio2 = Radiobutton(self,text="Medium",value=2)
        self.radio2.grid(column = 1,row = 3, sticky = W)
        self.radio3 = Radiobutton(self,text="Bad",value=3)
        self.radio3.grid(column = 2,row = 3, sticky = W)
        
        self.addLabel = Label(self,text="Summ the numbers entered in the below entries")
        self.addLabel.grid(columnspan=1,row=4,column=0)
        
        self.firstNum = Entry(self,width=5)
        self.firstNum.grid(row=5,column=0)
        
        self.plusLabel = Label(text="+")
        self.plusLabel.grid(row=5,column=1)
        
        self.secondNum=Entry(self,width=5)
        self.secondNum.grid(row=5,column=2)
        
        self.equalButton = Button(text="=")
        self.equalButton.bind("<Button-1>",self.summ)
        self.equalButton.grid(row=5,column=3)
        
        self.summLabel = Label(self,text="summ")
        self.summLabel.grid(row=5,column=4)
        
        
        
    
    def update_count(self,event):
        """Increase count and display new total"""
        self.buttonClicks = self.buttonClicks + 1
        self.button1["text"] = "total clicks: " + str(self.buttonClicks)
        self.label["text"] = "Here you can see number of clicks in a label: " + str(self.buttonClicks)
    
    def summ(self,event):
        num1 = int(self.firstNum.get())
        num2= int(self.secondNum.get())
        
        added = num1 + num2
        
        self.summLabel["text"] = str(added)

        
        
        
root = Tk()
root.title("OOP gui test")
root.geometry("500x600")
app = Application(root)

root.mainloop()