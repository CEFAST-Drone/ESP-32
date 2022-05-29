import socket
from machine import Pin

def connect(ssid, password):

  # Debug functions
  import esp
  esp.osdebug(None)

  import gc
  gc.collect()

  # Real connection
  import network
  import time

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

def run(img, port=80): # Create server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port)) # Local host is '', and 80 is the port
    s.listen(5)

    print('Config did.')

    while True: # Request/Responses loop
        print('...') # Waiting connection

        conn, addr = s.accept() # Requested activated
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)

        response = img
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: image/jpg\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()