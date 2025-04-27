#run periodic back ground tasks from tkinter gui

from tkinter import *
import ttkbootstrap as ttkb

from ttkbootstrap.scrolled import ScrolledText
import tkinter as tk

from time import sleep    

count = 0

def update_function():

    global count
    count = count + 1

    background_actions_textbox.insert(END,f'Read from Dummy Sensor,Value = {count}\n')
    background_actions_textbox.see(tk.END) #for auto  scrolling

    # sleep(5)
    root.after(100, update_function) # run itself again after 100 ms

def button_1_handler():
    my_button_text.insert(END,f'You Pressed Button 1\n')# add text
    my_button_text.see(tk.END) #for auto  scrolling

def button_2_handler():
    my_button_text.insert(END,f'You Pressed Button 2\n')# add text
    my_button_text.see(tk.END) #for auto  scrolling


   
root = ttkb.Window(themename = 'superhero') # theme = superhero
root.geometry('600x500')
root.title('Running Periodic background tasks in ttkbootstrap/tkinter')

#create textbox for button actions
my_button_text = ScrolledText(root,height = 4,width = 50,wrap = WORD,autohide = True)
my_button_text.pack(padx = 20,pady = 20)

#create button 
button_1 = ttkb.Button(text = 'Button 1',command = button_1_handler).pack(pady =10)
button_2 = ttkb.Button(text = 'Button 2',command = button_2_handler).pack(pady =10)

#create textbox for background actions
background_actions_textbox = ScrolledText(root,height = 10,width = 50,wrap = WORD,autohide = True)
background_actions_textbox.pack(padx = 20,pady = 20)

update_function() #call update function to start root.after() method

root.mainloop()