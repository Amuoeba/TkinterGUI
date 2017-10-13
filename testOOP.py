# -*- coding: utf-8 -*-
from tkinter import *

class Application (Frame):
    def __init__(self,master):
        """Initializes the frame"""
        Frame.__init__(self,master)
        self.grid()
        self.buttonClicks = 0
        self.create_widgets()
        
        
    def create_widgets(self):
        """Create button that counts number of clicks"""
        self.label = tk.Label(self, text= "this is a lable" + str(self.buttonClicks))
        self.label.grid()
        self.button1 = Button(self,text="total clicks " + str(self.buttonClicks))
        self.button1["command"] = self.update_count
        self.button1.grid()
        
        
    
    def update_count(self):
        """Increase count and display new total"""
        self.buttonClicks = self.buttonClicks + 1
        self.button1["text"] = "total clicks: " + str(self.buttonClicks)
        self.label["text"] = "Here you can see number of clicks in a label: " + str(self.buttonClicks)

        
        
        
root = Tk()
root.title("OOP gui test")
root.geometry("500x100")
app = Application(root)

root.mainloop()