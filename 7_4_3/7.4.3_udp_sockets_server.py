'''
run this server as you would any other 
python script and expecet the Waiting 
for connection line. In another terminal
run `nc -u 0.0.0.0 1337` to connect to the 
open socket and after doing so start typing
'''


import socket

# Start a socket object using IPv4 properties and UDP protocol
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind to our local computer on IP 0.0.0.0, port 1337
sock.bind(("0.0.0.0", 1337))



print('Waiting for incoming data')

while True:
    received, addr  = sock.recvfrom(1024) # we receive data on conn object, under the recv method, with at most 1024 bytes, when we do receive data we set it in this var
    received_message = received.decode('utf-8') # formatting string
    print("[RECEIVED]: "+ received_message.strip())
    sock.sendto(str.encode("You said: " + received_message), addr)    

sock.close()
