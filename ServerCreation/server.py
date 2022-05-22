import socket
from machine import Pin

def web_page(img): # HTML page
  
  return img

def run(img): # Create server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80)) # Local host is '', and 80 is the port
    s.listen(5)

    print('Config did.')

    while True: # Request/Responses loop
        print('...') # Waiting connection

        conn, addr = s.accept() # Requested activated
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)

        response = web_page(img)
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: image/jpg\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()