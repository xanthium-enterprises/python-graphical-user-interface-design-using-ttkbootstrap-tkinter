from tkinter import PhotoImage       #for PhotoImage()
#from tkinter import *
import ttkbootstrap as ttkb


root = ttkb.Window()                   
root.title('ttkbootstrap Images Demo') # Window Name
root.geometry('600x400')


# Creating a photoimage object to use image 
photo_object = PhotoImage(file = "robot.png") #create a photo image object

label1 = ttkb.Label(image = photo_object)# image parameter specifies the image that will be displayed on the label

label1.pack(pady = 10)

root.mainloop()