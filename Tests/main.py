from machine import Pin
import time

flash = Pin(4, Pin.OUT)

while True:
    time.sleep(1)
    print('Turn ON')
    flash.on()

    time.sleep(1)
    print('Turn OFF')
    flash.off()