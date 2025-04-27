#Adding and Deleting Records from a Table
# (c) www.xanthium.in


# Requires ttkbootstrap for running the code
# Install  ttkbootstrap using pip
# pip install ttkbootstrap
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

def Add_Record_Button_Handler():
    # add a single row 
    new_row_data = ('New John Doe',280, 'New.doe@example.com') # has to be a tuple ,not a list
    data_table.insert_row(index = 0,values = new_row_data)     #insert data to the first row row 0
    data_table.load_table_data()                               # call Tableview.load_table_data() to update the current view.
    

def Del_Record_Button_Handler():
    data_table.delete_row(index = 0) #Delete the first row
    
    
root   = ttk.Window()
root.title(' Tableview Add Delete Rows') # Window Name
root.geometry('800x520')

colors = root.style.colors

column_headers = [
                    {"text": " Name"            , "stretch": True, "anchor": "center"},
                    {"text": " Age"             , "stretch": True, "anchor": "center"},
                    {"text": " Email"           , "stretch": True, "anchor": "center"},
                    
                 ]

row_data = [
                ('John Doe'    , 28, 'johnqwertyuiohj67895tg.doe@example.com'),
                ('Jane Smith'  , 34, 'jane.smith@example.com'   ),
                ('Sarah Davis' , 29, 'sarah.davis@example.com'  ),
                ('David Wilson', 33, 'david.wilson@example.com' ),
                ('Linda Moore' , 38, 'linda.moore@example.com'  ),
                ('James Taylor', 25, 'james.taylor@example.com' ),
                ('Rachel Clark', 36, 'rachel.clark@example.com' ),
                
            ]

Add_Record_Button    = ttk.Button(text = 'Add a Row '   ,command = Add_Record_Button_Handler, bootstyle = PRIMARY)
Delete_Record_Button = ttk.Button(text = 'Delete a Row ',command = Del_Record_Button_Handler, bootstyle = DANGER)

data_table  = Tableview(
                         master     = root,
                         coldata    = column_headers,
                         rowdata    = row_data,
                         pagesize   = 10,
                         height     = 10,
                         autofit    = True,
                         paginated  = True,
                         searchable = True,
                         bootstyle  = SUCCESS,
                         
                         stripecolor = (colors.light, None),
                        )



data_table.pack(fill = BOTH, expand = NO, padx = 15, pady = 15)

Add_Record_Button.pack(pady =10)
Delete_Record_Button.pack(pady =10)


root.mainloop()




