import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


print("Ready")

# loop to sends messages one after another to the server

while True: 
    message = input("[SEND]: ") # we ask for user input
    sock.sendto(str.encode(message), ("0.0.0.0", 1337))
    received = sock.recvfrom(1024) # we get our response from the server
    print(received[0].decode("utf-8")) # we decode it, in this case we received a tuple so we access the first item, which is the message

socket.close()
