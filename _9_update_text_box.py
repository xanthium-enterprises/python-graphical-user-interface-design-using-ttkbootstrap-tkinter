from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap.scrolled import ScrolledText
import tkinter as tk
   
import random


def update_text():
    num = random.random()
    my_text.insert(END,f'Helloo {num},\n')# add text
    my_text.see(tk.END)
    root.after(1000, update_text) # run itself again after 1000 ms
    

root = ttkb.Window(themename = 'superhero') # theme = superhero
root.title('ttkbootstrap Scrolled Text  Demo')     # Window Name
root.geometry('800x500')
root.resizable(0,0)

# Define the font family and font size
font_family = 'Helvetica'
font_size = 15

my_text = ScrolledText(root,height = 10,width = 100,wrap = WORD,autohide = True,font=(font_family, font_size))
#ScrolledText.configure(font=(font_family, font_size)) 
update_text()

my_text.pack(pady = 20)

root.mainloop()