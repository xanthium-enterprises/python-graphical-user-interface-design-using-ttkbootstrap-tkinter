#add  Multiple rows into the table

# (c) www.xanthium.in


# Requires ttkbootstrap for running the code
# Install  ttkbootstrap using pip
# pip install ttkbootstrap

import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *



root   = ttk.Window()
root.title(' Tableview Add Multiple Rows') # Window Name
root.geometry('600x400')

colors = root.style.colors

column_headers = [
                    {"text": " Name"            , "stretch": True, "anchor": "center"},
                    {"text": " Age"             , "stretch": True, "anchor": "center"},
                    {"text": " Email"           , "stretch": True, "anchor": "center"},
                    
                 ]

row_data = [
                ('John Doe',      28, 'johnqwertyuiohj67895tg.doe@example.com'),
                ('Jane Smith',    34, 'jane.smith@example.com'),
                
            ]

data_table  = Tableview(
                         master     = root,
                         coldata    = column_headers,
                         rowdata    = row_data,
                         pagesize   = 10,
                         autofit    = True,
                         paginated  = True,
                         searchable = True,
                         bootstyle  = SUCCESS,
                         
                         stripecolor = (colors.light, None),
                        )




# add a Multiple rows 
new_row_data = [('New John Doe 1 ',280, 'New.doe_1@example.com'),
                ('New John Doe 2 ',380, 'New.doe_2@example.com'),
                ('New John Doe 3 ',480, 'New.doe_3@example.com'),
                ('New John Doe 4 ',580, 'New.doe_4@example.com'),
                
                ]# has  a list

data_table.insert_rows(index = 0,rowdata = new_row_data)     #insert data to the first row row 0
#data_table.insert_rows(index = 'end',rowdata = new_row_data)  #insert data to the last row ,index = 'end'

data_table.load_table_data() # call Tableview.load_table_data() to update the current view.


data_table.pack(fill = BOTH, expand = YES, padx = 15, pady = 15)

root.mainloop()


