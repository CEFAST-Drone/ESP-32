# .py file to run when the ESP is booted, to take a picture and save it in the os local

import shott
import tools
import os
from machine import Pin
import time

try:
    # Mount SD card
    tools.loadSD()

    # Take picture
    dirList = os.listdir()
    count = 0 # defining the name of the photo

    for f in dirList:
        if "photo" in f and f[0] == "p" and ".jpg" in f:
            count += 1
    
    filename = "photo" + str(count)

    shott.take_photo(filename, quality=10, brightness=2, saturation=-2, contrast=-1)

    # Move to SD card
    tools.move(filename + ".jpg", "sd/" + filename + ".jpg")
    
    flash = Pin(4, Pin.OUT)

    flash.on()
    time.sleep(1)
    flash.off()

    print("\nPhoto taked and moved to the SD card.\n")

except Exception as e:
    print(e)
