import tkinter as tk
import ttkbootstrap as ttkb

# Create the main window
root = ttkb.Window()
root.title('Check Button Example')
root.geometry('400x300')

# Function to handle the check button state change
def on_check_button_select():
    print(f'Option 1 = {chk_var1.get()}')
    print(f'Option 2 = {chk_var2.get()}')
    print(f'Option 3 = {chk_var3.get()}')

# Create variables to track the state of the check buttons
chk_var1 = tk.BooleanVar() #True/False 
chk_var2 = tk.BooleanVar()
chk_var3 = tk.BooleanVar()

# Create Check Buttons
check_button1 = ttkb.Checkbutton(root,
                                 text     = "Option 1",
                                 variable = chk_var1,
                                 command  = on_check_button_select)
check_button1.pack(pady=10)

check_button2 = ttkb.Checkbutton(root,
                                 text     = "Option 2",
                                 variable = chk_var2,
                                 command  = on_check_button_select)
check_button2.pack(pady=10)

check_button3 = ttkb.Checkbutton(root,
                                 text     = "Option 3",
                                 variable = chk_var3,
                                 command  = on_check_button_select)
check_button3.pack(pady=10)

'''
# Start with some checkboxes selected (optional)
chk_var1.set(True)  # Option 1 is selected by default
chk_var2.set(False) # Option 2 is not selected by default
chk_var3.set(True)  # Option 3 is selected by default
'''
# Run the application
root.mainloop()
