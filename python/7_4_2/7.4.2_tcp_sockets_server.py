'''
run this server as you would any other 
python script and expecet the Waiting 
for connection line. In another terminal
run `nc 0.0.0.0 1337` to connect to the 
open socket and after doing so start typing
'''


import socket

# Start a socket object using IPv4 properties and TCP protocol
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind to our local computer on IP 0.0.0.0, port 1337
sock.bind(("0.0.0.0", 1337))
# Start listening with a backlog size of 10
sock.listen(10)

conn = False # to check if we have got a connection yey

while True:
    if conn is False:
        print('Waiting for connection')
        conn, client = sock.accept() # waiting to accept a connection request, when connected we return conn  and client
        print('Connection from', client) # we output said information
    else:
        received = conn.recv(1024) # we receive data on conn object, under the recv method, with at most 1024 bytes, when we do receive data we set it in this var
        print(received)


sock.close()
