from machine import Pin
import time

flash = Pin(4, Pin.OUT)

while True:
    time.sleep(2)
    print('on')
    flash.on()
    time.sleep(2)
    print('off')
    flash.off()