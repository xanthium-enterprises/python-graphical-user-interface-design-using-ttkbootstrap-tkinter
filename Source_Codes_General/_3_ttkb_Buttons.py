from tkinter import *
import ttkbootstrap as ttkb

def button_1_handler():
    #print('You Clicked Me')
    clicked_label.config(text = 'You Clicked Me')
    


root = ttkb.Window(themename = 'superhero') # theme = superhero
root.title('ttkbootstrap Buttons Demo')     # Window Name
root.geometry('800x500')
root.resizable(0,0)                         # do not want to resize the window

site_addr_label = ttkb.Label(text = 'www.xanthium.in',font = ('Helvetica',14)).place(x=625,y=465)

#label
clicked_label = ttkb.Label(text = '-?-',font = ('Helvetica',20))
clicked_label.place(x=130,y=18) #do this here instead of above

#create button 
button_1 = ttkb.Button(text = 'Click Me',command = button_1_handler).place(x=20,y=20)


root.mainloop()