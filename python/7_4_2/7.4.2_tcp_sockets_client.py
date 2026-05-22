import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("0.0.0.0", 1337))# instead of bind we connect

print("Connected Succesfully")

# loop to sends messages one after another to the server

while True: 
    message = input("[SEND]: ") # we ask for user input
    sock.send(str.encode(message))
    received = sock.recv(1024) # we get our response from the server
    print(received.decode("utf-8")) # we decode it

socket.close()
