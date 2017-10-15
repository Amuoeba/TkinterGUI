# -*- coding: utf-8 -*
import tkinter as tk

class Application (tk.Frame):
    def __init__(self,master):
        """Initializes the frame"""
        tk.Frame.__init__(self,master)
        self.buttonClicks = 0
        self.create_widgets()
        self.grid()
        
        
    def create_widgets(self):
        """Create button that counts number of clicks"""
        self.label = tk.Label(self, text= "this is a lable " + str(self.buttonClicks))
        self.label.grid(columnspan=20,row=0,sticky=tk.W,padx=10,pady=20)
        
        self.entrs = tk.Entry(self,width=10)
        self.entrs.grid(row = 1,column = 0, padx = 20, sticky = tk.W)
        
        self.button1 = tk.Button(self,text="total clicks " + str(self.buttonClicks))
        self.button1.bind("<Button-1>",self.update_count)
        self.button1.grid(column = 0,row = 2,sticky = tk.W)
        
        self.radio1 = tk.Radiobutton(self,text="Good",value=1)
        self.radio1.grid(column = 0,row = 3, sticky = tk.W)
        self.radio2 = tk.Radiobutton(self,text="Medium",value=2)
        self.radio2.grid(column = 1,row = 3, sticky = tk.W)
        self.radio3 = tk.Radiobutton(self,text="Bad",value=3)
        self.radio3.grid(column = 2,row = 3, sticky = tk.W)
        
        self.addLabel = tk.Label(self,text="Summ the numbers entered in the below entries")
        self.addLabel.grid(columnspan=20,row=4,column=0)
        
        self.firstNum = tk.Entry(self)
        self.firstNum.grid(row=5,column=0,sticky=tk.W)
        
        self.plusLabel = tk.Label(self,text="+")
        self.plusLabel.grid(row=5,column=1)
        
        self.secondNum=tk.Entry(self)
        self.secondNum.grid(row=5,column=2,sticky=tk.W)
        
        self.equalButton = tk.Button(self,text="=")
        self.equalButton.bind("<Button-1>",self.summ)
        self.equalButton.grid(row=5,column=3,sticky=tk.W)
        
        self.summLabel = tk.Label(self,text="summ")
        self.summLabel.grid(row=5,column=4,sticky=tk.W)
        
        
        
        
        
    
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

        
        
        
root = tk.Tk()
root.title("OOP gui test")
root.geometry("500x600")
app = Application(root)

root.mainloop()