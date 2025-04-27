from tkinter import *
import ttkbootstrap as ttkb

#dark themes
root = ttkb.Window(themename = 'superhero') # theme = superhero
#root = ttkb.Window(themename = 'darkly')
#root = ttkb.Window(themename = 'vapor')

#light themes
#root = ttkb.Window(themename = 'cosmo')
#root = ttkb.Window(themename = 'litera')
#root = ttkb.Window(themename = 'yeti')

root.title('My ttkbootstrap Window')
root.geometry('800x500') #Width

# this removes the maximize button
root.resizable(0,0) #do not want to resize the window

#Create a Label
#https://ttkbootstrap.readthedocs.io/en/latest/styleguide/
#bootstyle define colours

my_label = ttkb.Label(text = 'Hello World in Helvetica',font = ('Helvetica',20),bootstyle='light')
my_label.place(x=35,y=10)

my_label = ttkb.Label(text = 'Hello World in Ariel',font = ('Ariel',20),bootstyle='success')
my_label.place(x=35,y=70)

my_label = ttkb.Label(text = 'Hello World in Courier',font = ('Courier',20),bootstyle='danger').place(x=35,y=140)

root.mainloop()