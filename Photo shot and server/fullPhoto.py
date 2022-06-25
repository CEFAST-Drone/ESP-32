# .py file to run when the ESP is booted, to take a picture and save it in the os local

import shott
import tools
import os

def pic(q=10, b=2, s="", c="", nick=1, fast=0):
    try:
        # Mount SD card
        if not nick: tools.loadSD()

        # Take picture
        dirList = os.listdir("sd/")
        count = 0 # defining the name of the photo

        for f in dirList:
            if "photo" in f and f[0] == "p" and ".jpg" in f:
                count += 1
        
        filename = "sd/photo" + str(count)

        if nick: # Put the config in the filename
            filename += "-" + str(q) + "-" + str(b) + "-" + str(s) + "-" + str(c)

        shott.take_photo(filename, quality=q, brightness=b, saturation=s, contrast=c, dirLocal="sd/")

        # Move to SD card
        # tools.move(filename + ".jpg", "sd/" + filename + ".jpg") - Do not need by saving it in the sdCard instead of in the flash memory
        
        if not fast:
            from machine import Pin
            import time

            flash = Pin(4, Pin.OUT)

            flash.on()
            time.sleep(0.5)
            flash.off()

        print("\nPhoto taked and moved to the SD card.\n")

    except Exception as e:
        print(e)
