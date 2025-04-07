#Delete row inthe table
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
                ('Sarah Davis',   29, 'sarah.davis@example.com', ),
                ('David Wilson',  33, 'david.wilson@example.com', ),
                ('Linda Moore',   38, 'linda.moore@example.com',  ),
                ('James Taylor',  25, 'james.taylor@example.com', ),
                ('Rachel Clark',   36, 'rachel.clark@example.com',),
                
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





data_table.delete_row(index = 0)





data_table.pack(fill = BOTH, expand = YES, padx = 15, pady = 15)

root.mainloop()



