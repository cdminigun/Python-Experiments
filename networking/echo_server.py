import socket
import argparse

class SocketCon:
    def __init__(self, port, address, client_address):
        self.port = port
        self.addr = address
        self.client_address = client_address
        self.sock = None
    def server_bind(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Intiates the socket object. 
        self.sock.bind((self.addr, self.port)) #Binds the server to the given address and port
        self.sock.listen(10) #10 concurrent hosts can be connetected
        while 1:
            client, addr = self.sock.accept()
            data_in = client.recv(1024)
            print data_in
            client.send(data_in)
        self.sock.close()

    def client_connect(self, message):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.addr, self.port))
        self.sock.send(message)
        data = self.sock.recv(1024)
        print data
        self.sock.close()
def test_address(address):
    test = address.split('.')
    if len(test) == 4:
        return 1
    else:
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket Template: Change me")
    parser.add_argument("-p", "--port", type=int, default="1337", help="The port that you want to bind on.")
    parser.add_argument("-a", "--address", type=str, default="0.0.0.0", help="The address that you want to bind to.")
    parser.add_argument("-c", "--connection_type", type=int, default=1, help="Type of connection. 1 - Server, 2 - Client")


    args = parser.parse_args()
    if args.address and test_address(args.address):
        if args.connection_type:
            if args.connection_type == 1:
                pass
            elif args.connection_type == 2:
                pass
            else:
                print "some error message"
        else:
            print "some error message"
    else:
        print "some error message"

