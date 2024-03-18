#Show last Character Scrolling

from tkinter import *
import ttkbootstrap as ttkb

from ttkbootstrap.scrolled import ScrolledText
import tkinter as tk
   

count = 0

def button_1_handler():
    global count
    count = count + 1
    text_box.insert(END,f'You Pressed Button  {count} times\n')# add text
    text_box.see(tk.END) #for auto  scrolling




   
root = ttkb.Window(themename = 'superhero') # theme = superhero
root.geometry('400x300')
root.title('Auto Scrolling Text Box ')

#create textbox for button actions
text_box = ScrolledText(root,height = 5,width = 50,wrap = WORD,autohide = True)
text_box.pack(padx = 20,pady = 20)

#create button 
button_1 = ttkb.Button(text = 'Press Me',command = button_1_handler).pack(pady =10)


root.mainloop()