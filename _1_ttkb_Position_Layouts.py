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
root.geometry('800x500')

#Create a Label

#Positioning Widgets With Grid Layout Manager

my_label = ttkb.Label(text = 'Hello World',font = ('Helvetica',28),width=10)
my_label.grid(row=0, column=0) #Positioning Widgets With Grid Layout Manager

my_label2 = ttkb.Label(text = 'ttkBootstrap',font = ('Courier',18),width=15)
my_label2.grid(row=1, column=0) #Positioning Widgets With Grid Layout Manager

#Positioning Widgets With Place Layout Manager
my_label3 = ttkb.Label(text = 'Place Layout',font = ('Courier',18))
my_label3.place(x=50,y=100) #Positioning Widgets With Place Layout Manager

my_label3 = ttkb.Label(text = 'Place Layout2',font = ('Courier',18))
my_label3.place(x=50,y=150) #Positioning Widgets With Place Layout Manager

root.mainloop()