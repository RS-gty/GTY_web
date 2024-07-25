import string

import numpy as np
import random


class Atom(object):
    def __init__(self):
        self.servers = []
        self.server_id = []
        self.message = []
        self.time = 0

    def update(self):
        self.time += 1

    def id_generator(self):
        return ''.join(random.sample(string.ascii_letters, 8))

    def recieve_message(self, server_id, message):
        self.message.append([message, server_id])



class Server(object):
    def __init__(self):
        self.time = 0
        self.atoms = []
        self.ids = []

    def register(self, atom: Atom, server_id='default'):
        if server_id == 'default':
            s_id = ''.join(random.sample(string.ascii_letters, 8))
            server_id = s_id
        atom.servers.append(self)
        atom.server_id.append(server_id)
        self.atoms.append(atom)
        self.ids.append(server_id)

    def send_message(self, message, atoms=None):
        if atoms is None:
            for atom in self.atoms:
                atom.recieve_message(self.ids[self.atoms.index(atom)], message)
        else:
            for atom in atoms:
                atom.recieve_message(self.ids[self.atoms.index(atom)], message)


def main():
    A1 = Atom()
    S1 = Server()
    S1.register(A1)
    S1.send_message('Hello, world!')
    print(A1.message, S1.ids)



if __name__ == '__main__':
    main()
