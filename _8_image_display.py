from tkinter import *
import ttkbootstrap as ttkb


root = ttkb.Window(themename = 'superhero') # theme = superhero
root.title('ttkbootstrap images Demo')     # Window Name
root.geometry('800x500')
root.resizable(0,0)

# Creating a photoimage object to use image 
photo = PhotoImage(file = "robot.png") #only png files

my_label = ttkb.Label(text = 'Only png files\nallowed',font = ('Helvetica',20))
my_label.place(x=35,y=10)


#Label
my_label = ttkb.Label(text = 'PNG Images',image =photo,font = ('Helvetica',20))
my_label.pack(pady =10)



root.mainloop()
