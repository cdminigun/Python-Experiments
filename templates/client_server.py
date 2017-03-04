import argparse
import socket

def client_socket():
    print "This is my client socket"
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 2000))
    client_socket.send("hello")

def server_socket():
    print "This is my server socket"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("0.0.0.0", 2000)) #MAX_SHORT ~65535
    sock.listen(10)
    while 1:
        conn, addr = sock.accept()
        a = conn.recv(1024)
        print a

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Client and Server template.")
    parser.add_argument("-t", "--type_of_socket", type=str, help="The input for type of socket you want. Options: Client or Server")
    parser.add_argument("-p", "--print_this_string", type=str, help="prints this string")
    args = parser.parse_args()
    if not args.type_of_socket and args.print_this_string:
        parser.print_help()
        exit()
    print args.print_this_string 

    if "client" in args.type_of_socket.lower():
        client_socket()
    elif args.type_of_socket and "server" in args.type_of_socket.lower():
        server_socket()
    else:
        parser.print_help()

