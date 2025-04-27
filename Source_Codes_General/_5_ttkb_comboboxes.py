#comboboxes

from tkinter import *
import ttkbootstrap as ttkb

def click_bind(e):
    print(f'You selected {my_combo.get()}')


root = ttkb.Window(themename = 'superhero') # theme = superhero
root.title('ttkbootstrap Buttons Demo')     # Window Name
root.geometry('800x500')
root.resizable(0,0)

#create Dropdown options
options = ['1200','2400','4800','9600']

#create Combobox
my_combo = ttkb.Combobox(values = options)
my_combo.pack(pady =50)
my_combo.current(3)#set the default value on combobox

#bind the combobox
my_combo.bind('<<ComboboxSelected>>',click_bind)

root.mainloop()