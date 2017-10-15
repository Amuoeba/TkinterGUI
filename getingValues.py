# -*- coding: utf-8 -*-
import tkinter as tk

class Application (tk.Frame):
    def __init__(self,parent):
        """Initializes the frame"""
        tk.Frame.__init__(self,parent)
        self.parent=parent
        self.defVariables()        
        self.create_widgets()
        self.create_menu()
        self.grid()
    
    def quit_app(self):
        self.parent.destroy()
        
    def defVariables(self):
        self.checkVar = tk.BooleanVar()
        
    
    def create_menu(self):
        self.menuBar =tk.Menu(self.parent)
        self.fileMenu = tk.Menu(self.menuBar,tearoff=0)
        self.fileMenu.add_command(label="Open")
        self.fileMenu.add_command(label="Save")
        self.fileMenu.add_command(label="Quit",command = self.quit_app)
        
        self.menuBar.add_cascade(label="file",menu=self.fileMenu)
        self.parent.config(menu=self.menuBar)
        
        
        
        
        
        
        
    def create_widgets(self):
        self.strEntry = tk.Entry(self)
        self.strEntry.grid()
        
        self.numEntry = tk.Entry(self)
        self.numEntry.grid(row=0,column=1)
        
        self.CheckButton = tk.Checkbutton(self,text="switch",variable=self.checkVar)
        self.CheckButton.grid(column=2,row=0)
        
        self.button = tk.Button(self,text="Outputs")
        self.button.bind("<Button-1>",self.output)
        self.button.grid(row=0,column=3)
        
        #Text and scrollbar
        self.text=tk.Text(self,height=10,width=50)
        self.text.grid(row = 1,columnspan=30,sticky="nsew")
        
        scrollbar = tk.Scrollbar(self,command = self.text.yview)
        scrollbar.grid(row=1,column=31,sticky="nsew")
        self.text["yscrollcommand"]=scrollbar.set
        
        self.textDecoded=tk.Text(self,height=10,width=50)
        self.textDecoded.grid(row = 2,columnspan=30,sticky="nsew")
        
        scrollbarDecoded = tk.Scrollbar(self,command = self.textDecoded.yview)
        scrollbarDecoded.grid(row=2,column=31,sticky="nsew")
        self.textDecoded["yscrollcommand"]=scrollbarDecoded.set
        
        
    def output(self,event):
        strVar = str(self.strEntry.get())
        intVar = str(self.numEntry.get())
        boolVar = str(self.checkVar.get())
        textVar = str(self.text.get("1.0",tk.END))
        print("strVar: "+strVar + " " + " intVar: "+ intVar +" BoolVar: " +
              boolVar + " Text var: " , textVar) 

        
        
        
root = tk.Tk()
root.title("OOP gui test")
root.geometry("600x100+300+300")
app = Application(root)

root.mainloop()