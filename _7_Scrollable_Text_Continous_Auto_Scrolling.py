#run periodic back ground tasks from tkinter gui

from tkinter import *
import ttkbootstrap as ttkb

from ttkbootstrap.scrolled import ScrolledText
import tkinter as tk
   

count = 0



def update_function():

    global count
    count = count + 1 
    
    text_box.insert(END,f'Auto Scrolling Text Box,Value = {count}\n')
    text_box.see(tk.END) #for auto  scrolling

    root.after(600, update_function) # run itself again after 100 ms


   
root = ttkb.Window(themename = 'superhero') # theme = superhero
root.geometry('400x200')
root.title('Auto Scrolling Text Box ')

#create textbox for button actions
text_box = ScrolledText(root,height = 5,width = 50,wrap = WORD,autohide = True)
text_box.pack(padx = 20,pady = 20)

update_function()


root.mainloop()