#Basic Meter with text under it 

#As the attribute Image.CUBIC is deprecated (replaced by Image.BICUBIC) and removed in Pillow v10.0.0.
#Either install an older version (v9.5.0) of Pillow module
#or create the attribute explicitly before importing ttkbootstrap module:

from PIL import Image
Image.CUBIC = Image.BICUBIC

import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

root = ttkb.Window()

meter = ttkb.Meter(
                    metersize       = 300,       # Size of the meter
                    padding         = 50,        # distance between window edges
                    meterthickness  = 20,        # thickness of the meter dial
                    stripethickness = 00,        # thickness of discrete stripes,0=Continous
                    bootstyle       = "success", # allows you to apply pre-defined styles like primary,danger,success etc 
                    metertype       = "semi",    # Semicircle ,"full" =circular
                    
                    amounttotal     = 100,   #max value of scale =100
                    amountused      = 70,    #current value 
                    
                    
                    subtext        = "Text Written Below the Meter",
                    subtextstyle   = "primary",                      # allows you to apply pre-defined styles like primary,danger,success etc 
                    subtextfont    = "-size 10 -weight bold",
                    
                    
                    interactive    = True, #you can change meter position by mouse 
                 )


meter.pack()
root.mainloop()

