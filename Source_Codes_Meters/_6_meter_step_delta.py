#How to use the step () funtion to increment the meter

#step(self, delta=1)
#Increase the indicator value by delta
#The indicator will reverse direction and count down once it reaches the maximum value.

#As the attribute Image.CUBIC is deprecated (replaced by Image.BICUBIC) and removed in Pillow v10.0.0.
#Either install an older version (v9.5.0) of Pillow module
#or create the attribute explicitly before importing ttkbootstrap module:

from PIL import Image
Image.CUBIC = Image.BICUBIC

import ttkbootstrap as ttkb
from ttkbootstrap.constants import *



def increment_Button_handler():
    meter.step(1) #increment meter by 1
    
  

root = ttkb.Window()
root.title('Meter Control using Button') 
root.geometry('500x500') # width x height


meter = ttkb.Meter(
                    metersize       = 300,       # Size of the meter
                    padding         = 10,        # distance between window edges
                    meterthickness  = 20,        # thickness of the meter dial
                    stripethickness = 00,         # thickness of discrete stripes,0=Continous
                    bootstyle       = "success", # allows you to apply pre-defined styles like primary,danger,success etc 
                    metertype       = "full",    # Semicircle ,"full" =circular
                    
                    amounttotal     = 100,   #max value of scale =100
                    amountused      = 10,    #current value 
                    
                    
                    subtext        = "Text Written Below the Meter",
                    subtextstyle   = "primary",                      # allows you to apply pre-defined styles like primary,danger,success etc 
                   
                   )

Increment_Button = ttkb.Button(text = 'Increment Meter',command = increment_Button_handler)


meter.pack()

Increment_Button.pack(pady = 5)

root.mainloop()

