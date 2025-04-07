#Creating Radio Button using Tkinter

import ttkbootstrap as ttkb
import tkinter as tk

root = ttkb.Window()

root.title('Radio Button Handling in ttkbootstrap') 
root.geometry('500x300')                             # width x height

#function to handle the Radio Button Selection
def on_radio_select():
    print(radio_button_var.get())
    

radio_button_var = tk.StringVar() #create a variable radio_button_var of type tk.StringVar()

# Create the radio buttons
radio_button1 = ttkb.Radiobutton(root,
                                 text     = "Radio Button Option 1",
                                 value    = "Option 1",
                                 variable = radio_button_var,
                                 command  = on_radio_select)
radio_button1.pack(pady=10)

radio_button2 = ttkb.Radiobutton(root,
                                 text     ="Radio Button Option 2",
                                 value    = "Option 2",
                                 variable = radio_button_var,
                                 command  = on_radio_select)

radio_button2.pack(pady=10)

radio_button3 = ttkb.Radiobutton(root,
                                 text     = "Radio Button Option 3",
                                 value    = "Option 3",
                                 variable = radio_button_var,
                                 command  = on_radio_select)
radio_button3.pack(pady=10)

# Optional: Set a default selected value
#radio_button_var.set("Option 3")

root.mainloop()