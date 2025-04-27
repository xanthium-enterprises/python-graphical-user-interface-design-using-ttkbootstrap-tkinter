# ttkbootstrap Entry Widget
# requires ttkbootstrap installed on your system 

from tkinter import *
import ttkbootstrap as ttkb

def button_1_handler():
    print(f'You Typed in {My_Entry.get()}')
    clicked_label.config(text = f'You Typed in {My_Entry.get()}')

root = ttkb.Window(themename = 'superhero') # theme = superhero
root.title('ttkbootstrap Buttons Demo')     # Window Name
root.geometry('800x500')
root.resizable(0,0)                         # do not want to resize the window

#label
clicked_label = ttkb.Label(text = '-?-',font = ('Helvetica',20))
clicked_label.pack()

#Create Entry Widget 
My_Entry = ttkb.Entry(root)
My_Entry.insert(0,'Hello')

My_Entry.pack()

#Create Button

button_1 = ttkb.Button(text = 'Click Me',command = button_1_handler)
button_1.pack()

root.mainloop()