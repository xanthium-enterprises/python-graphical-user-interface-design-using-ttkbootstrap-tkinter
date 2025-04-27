from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap.scrolled import ScrolledText


root = ttkb.Window(themename = 'superhero') # theme = superhero
root.title('ttkbootstrap Scrolled Text  Demo')     # Window Name
root.geometry('800x500')
root.resizable(0,0)

my_text = ScrolledText(root,height=10,width=100,wrap =WORD,autohide=True)

my_text.insert(END,'Helloo,type something\n')# add text
my_text.insert(END,'Helloo,type something')# add text


text =my_text.get('1.0',END)#get all the text from the widget
#The first part, "1.0" means that the input should be read from line one, character zero (ie: the very first character).
#END is an imported constant which is set to the string "end". The END part means to read until the end of the text box is reached.
#The only issue with this is that it actually adds a newline to our input.
#So, in order to fix it we should change END to end-1c(Thanks Bryan Oakley) The -1c deletes 1 character, while -2c would mean delete two characters, and so on.
#

print(text)
my_text.pack(pady =20)

root.mainloop()