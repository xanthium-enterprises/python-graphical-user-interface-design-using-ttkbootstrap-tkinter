# Create a Large ttkbootstrap table and display data with pagination
# (c) www.xanthium.in


# Requires ttkbootstrap for running the code
# Install  ttkbootstrap using pip
# pip install ttkbootstrap


import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

root   = ttk.Window()
root.title('ttkbootstrap Tableview Widget Demo') # Window Name
#root.geometry('800x800')
colors = root.style.colors

column_headers = [
                    {"text": " Name"            , "stretch": True, "anchor": "center"},
                    {"text": " Age"             , "stretch": True, "anchor": "center"},
                    {"text": " Email"           , "stretch": True, "anchor": "center"},
                    {"text": " Address"         , "stretch": True, "anchor": "center"},
                    {"text": " Phone Number"    , "stretch": True, "anchor": "center"},
                 ]

row_data = [
                ('John Doe',      28, 'johnqwertyuiohj67895tg.doe@example.com',      '1234 Elm Street, Springfield'  , '(555) 123-4567'),
                ('Jane Smith',    34, 'jane.smith@example.com',    '5678 Oak Avenue, Metropolis'   , '(555) 987-6543'),
                ('Emily Johnson', 22, 'emily.johnson@example.com', '9101 Pine Road, Rivertown'     , '(555) 555-1234'),
                ('Michael Brown', 41, 'michael.brown@example.com', '2345 Maple Street, Smalltown'  , '(555) 223-4567'),
                ('Sarah Davis',   29, 'sarah.davis@example.com',   '6789 Birch Avenue, Lakeside'   , '(555) 876-5432'),
                ('David Wilson',  33, 'david.wilson@example.com',  '1357 Cedar Drive, Uptown'      , '(555) 111-2233'),
                ('Linda Moore',   38, 'linda.moore@example.com',   '2468 Pine Hill, Midtown'       , '(555) 444-5678'),
                ('James Taylor',  25, 'james.taylor@example.com',  '3690 Elm Lane, Rivertown'      , '(555) 999-1234'),
                ('Rachel Clark',   36, 'rachel.clark@example.com', '4812 Oak Road, Hilltop'        , '(555) 555-7890'),
                ('Christopher Lewis', 30, 'christopher.lewis@example.com', '1023 Cherry Street, Downtown', '(555) 333-4455'),
                ('Samantha Green', 27, 'samantha.green@example.com', '7890 Maple Road, Westfield'        , '(555) 777-1122'),
                ('Daniel Lee',     31, 'daniel.lee@example.com', '2221 Pine Ridge, Brookside'            , '(555) 321-4567'),
                ('Olivia Martinez', 40, 'olivia.martinez@example.com', '4200 Cedar Drive, Oldtown'       , '(555) 654-7890'),
                ('Sophia Brown',    23, 'sophia.brown@example.com', '3421 Oak Lane, Rivertown'           , '(555) 876-4321'),
                ('Jack Wilson', 35, 'jack.wilson@example.com', '1156 Birch Avenue, Northside'            , '(555) 231-6789'),
                ('Emma Scott', 29, 'emma.scott@example.com', '1345 Pine Avenue, Lakeside'                , '(555) 444-1234'),
                ('Henry White', 45, 'henry.white@example.com', '2777 Maple Street, West Hills'           , '(555) 555-6789'),
                ('Ava Hall', 32, 'ava.hall@example.com', '8902 Cedar Lane, Greenfield'                   , '(555) 666-7890'),
                ('Ethan Harris', 28, 'ethan.harris@example.com', '1035 Elmwood Drive, Midtown'           , '(555) 777-3345'),
                ('Mason Allen', 37, 'mason.allen@example.com', '2468 Oakwood Street, Hillside'           , '(555) 555-1122'),
                ('Isabella Young', 24, 'isabella.young@example.com', '7823 Birch Road, Riverbend'        , '(555) 888-1234'),
                ('Liam King', 34, 'liamisabellamasonhenry_white.king@example.com', '3322 Pine Avenue, Southgate'                 , '(555) 222-3456'),
            
            ]

data_table  = Tableview(
                         master     = root,
                         coldata    = column_headers,
                         rowdata    = row_data,
                         pagesize   = 10,               # display 10 row entries per page
                         height     = 5,                # displays onl5 of the 10 rows,rest you have to scroll down
                         autofit    = True,
                         paginated  = True,             # organize into pages,each page will have 10 rows as specified in pagesize   = 10,  
                         searchable = True,             # Searchbox = True
                         bootstyle  = SUCCESS,
                         
                         stripecolor = (colors.light, None), #alternate rows coloured in light shade for easy reading
                        )

data_table.pack(fill = BOTH, expand = YES, padx = 15, pady = 15)

root.mainloop()
