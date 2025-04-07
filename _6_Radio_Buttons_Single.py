import ttkbootstrap as ttkb
import tkinter as tk

root = ttkb.Window()

#function to handle the Radio Button Selection
def on_radio_select():
   print(radio_button_var.get())
   
radio_button_var = tk.StringVar() #create a variable radio_button_var of type tk.StringVar()

# Create the radio button
radio_button1 = ttkb.Radiobutton(root,
                                 text     = "Radio Button Option 1",
                                 value    = "Option 1",
                                 variable = radio_button_var,
                                 command  = on_radio_select)
radio_button1.pack(pady = 30)                             
root.mainloop()