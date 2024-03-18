from tkinter import *
import ttkbootstrap as ttkb


root = ttkb.Window(themename = 'superhero') # theme = superhero
root.title('ttkbootstrap Buttons Demo')     # Window Name
root.geometry('800x500')
root.resizable(0,0)

#Label
my_label = ttkb.Label(text = 'Label 1',font = ('Helvetica',20))
my_label.pack()

#Seperator
my_sep = ttkb.Separator(root,bootstyle = 'danger',orient = 'horizontal')
my_sep.pack(fill = 'x',padx = 30)

#Label
my_label2 = ttkb.Label(text = 'Label 2',font = ('Helvetica',20))
my_label2.pack()

#Seperator
my_sep = ttkb.Separator(root,bootstyle = 'primary',orient = 'vertical')
my_sep.pack(fill = 'y')

root.mainloop()