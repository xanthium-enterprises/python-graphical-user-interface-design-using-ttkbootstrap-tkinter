#read text from ScrolledText


from tkinter import *
import ttkbootstrap as ttkb

from ttkbootstrap.scrolled import ScrolledText
import tkinter as tk
   
def button_1_handler():
    text = my_text.get('1.0',END) #get all the text from the ScrolledText widget
    print(text)


root = ttkb.Window(themename = 'superhero') # theme = superhero
root.geometry('800x500')

my_text = ScrolledText(root,height = 10,width = 100,wrap = WORD,autohide = True)
my_text.pack(pady = 20)



#create button 
button_1 = ttkb.Button(text = 'Read All Text',command = button_1_handler).pack(pady = 20)

root.mainloop()