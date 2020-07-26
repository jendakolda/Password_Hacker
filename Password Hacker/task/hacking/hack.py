# write your code here
import socket
import sys


class Hacker(object):

    def __init__(self, ip_address, port, msg):
        self.ip_address = ip_address
        self.port = int(port)
        self.msg = msg
        self.client_socket = socket.socket()
        self.address = (self.ip_address, self.port)

    def main(self):
        self.client_socket.connect(self.address)
        self.client_socket.send(self.msg.encode())
        response = self.client_socket.recv(1024)
        response = response.decode()
        print(response)

    def closing(self):
        self.client_socket.close()


args = sys.argv
start = Hacker(*args[1:])
start.main()
start.closing()
