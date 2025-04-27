import ttkbootstrap as ttkb

root = ttkb.Window(themename = 'litera')
root.geometry('400x200')                # widthxheight

My_Label_1 = ttkb.Label(text = "Helvetica       15",bootstyle = 'primary',font = ('Helvetica',15)      ).place(x=10,y=10) 
My_Label_2 = ttkb.Label(text = "Ariel           15",bootstyle = 'warning',font = ('Ariel',15)          ).place(x=10,y=40)  
My_Label_3 = ttkb.Label(text = "Times New Roman 15",bootstyle = 'danger' ,font = ('Times New Roman',15)).place(x=10,y=80) 
My_Label_4 = ttkb.Label(text = "Comic Sans MS   15",bootstyle = 'success' ,font = ('Comic Sans MS',15)  ).place(x=10,y=120)
My_Label_5 = ttkb.Label(text = "Courier New     15",bootstyle = 'dark'    ,font = ('Courier New',15)    ).place(x=10,y=160) 


root.mainloop()