import socket

HOST = "192.168.88.248"
PORT = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

while True:

    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024)
    print(f"The message from the client is: {message}")
    communication_socket.send(f"Got your message! Thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Communication with {address} ended")
