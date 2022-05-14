# Debug functions
import esp
esp.osdebug(None)

import gc
gc.collect()

# Real connection
import network
import time
from machine import Pin

ssid = 'teste'
password = 'ipoq6796'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(4, Pin.OUT) # Turn on some led (flashlight) to tell that internet was connected
led.value(1)
time.sleep(1)
led.value(0)