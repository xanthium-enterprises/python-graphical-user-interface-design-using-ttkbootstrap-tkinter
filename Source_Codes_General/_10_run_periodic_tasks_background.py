#run periodic back ground tasks from tkinter gui

import ttkbootstrap as ttkb

count = 0

def update_function():

    global count
    print(f'{count} Hello')
    count = count + 1

    root.after(100, update_function) # run itself again after 1000 ms

   
root = ttkb.Window(themename = 'superhero') # theme = superhero
root.geometry('800x500')

update_function()

root.mainloop()