# Testing all configs of the ESP32 camera

import fullPhoto

def test():
    for quality in [10, 63]:
        for brightness in [0, 1, 2]:
            for saturation in [-2, -1, 0, 1, 2]:
                for contrast in [0, 1, 2]:
                    fullPhoto.pic(q=quality, b=brightness, s=saturation, c=contrast, fast=1)
    
    fullPhoto.pic(nick=0) # Last pic to inform the end of the execution