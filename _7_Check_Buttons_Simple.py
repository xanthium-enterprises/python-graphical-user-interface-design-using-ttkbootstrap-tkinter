import tkinter as tk
import ttkbootstrap as ttkb

# Function to handle the check button state change
def on_check_button_select():
    print(f'Option 1 = {chk_var1.get()}')


# Create the main window
root = ttkb.Window()


chk_var1 = tk.BooleanVar() #True/False

# Create Check Buttons
check_button1 = ttkb.Checkbutton(root,
                                 text     = "Option 1", 
                                 variable = chk_var1,
                                 command  = on_check_button_select)
check_button1.pack(pady=10)

root.mainloop()