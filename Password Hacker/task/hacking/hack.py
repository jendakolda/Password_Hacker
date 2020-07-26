# write your code here
import socket
import sys


class Hacker(object):
    args = sys.argv
    ip_address = args[1]
    port = int(args[2])
    msg = args[3]
    msg = msg.encode()

    def __init__(self):
        self.client_socket = socket.socket()
        self.address = (self.ip_address, self.port)

    def main(self):
        self.client_socket.connect(self.address)
        self.client_socket.send(self.msg)
        response = self.client_socket.recv(1024)
        response = response.decode()
        print(response)

    def closing(self):
        self.client_socket.close()


start = Hacker()
start.main()
start.closing()
