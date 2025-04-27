# Create a simple ttkbootstrap table nd display data
# (c) www.xanthium.in


# Requires ttkbootstrap for running the code
# Install  ttkbootstrap using pip
# pip install ttkbootstrap



import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

root   = ttk.Window()
root.title('Window Name') # Window Name

colors = root.style.colors

#Name of the Columns
column_headers = [ " Name" ," Age"," Email"]
                    
                 
#Data to be added to the  rows
row_data = [
                ('John Doe',      28, 'johnqwertyuiohj67895tg.doe@example.com'),
                ('Jane Smith',    34, 'jane.smith@example.com'),
                ('Emily Johnson', 22, 'emily.johnson@example.com'),
                ('Michael Brown', 41, 'michael.brown@example.com'),
                ('Sarah Davis',   29, 'sarah.davis@example.com'),
            ]

data_table  = Tableview(
                         master     = root,
                         coldata    = column_headers,
                         rowdata    = row_data,
                         pagesize   = 5,
                         autofit    = True,
                         paginated  = True,
                         searchable = True,
                         bootstyle  = SUCCESS,
                         stripecolor = (colors.light, None),
                        )

data_table.pack(fill = BOTH, expand = NO, padx = 20, pady = 15)

root.mainloop()