import string

import numpy as np
import random


class Atom(object):
    def __init__(self):
        self.id = ''.join(random.sample(string.ascii_letters, 4))
        self.servers = []
        self.server_id = []
        self.__message = []
        self.time = 0

    def update(self):
        self.time += 1

    def id_generator(self):
        s = ''.join(random.sample(string.ascii_letters, 8))
        while s not in self.server_id:
            return s

    def receive_message(self, server_id, message, target):
        self.__message.append([message, server_id, target])

    def deliver_message(self, server_id):
        messages = []
        for message in self.__message:
            if message[2] is None or message[2] == server_id:
                messages.append(message)
        return messages

class Server(object):
    def __init__(self):
        self.time = 0
        self.atoms = []
        self.ids = []

    def register(self, atom: Atom):
        server_id = atom.id_generator()
        atom.servers.append(self)
        atom.server_id.append(server_id)
        self.atoms.append(atom)
        self.ids.append(server_id)

    def send_message(self, message, atoms=None, target=None):
        if atoms is None:
            for atom in self.atoms:
                atom.receive_message(self.ids[self.atoms.index(atom)], message, target)
        else:
            for atom in atoms:
                atom.receive_message(self.ids[self.atoms.index(atom)], message, target)

    def get_message(self, atoms=None):
        messages = []
        if atoms is None:
            for atom in self.atoms:
                messages.append(atom.deliver_message(self.ids[self.atoms.index(atom)]))
        else:
            for atom in self.atoms:
                messages.append(atom.deliver_message(self.ids[self.atoms.index(atom)]))
        return messages


def main():
    A1 = Atom()
    A2 = Atom()

    S1 = Server()
    S2 = Server()

    S1.register(A1)
    S2.register(A1)

    S1.send_message('Hello, S2!', target=S2.ids[S2.atoms.index(A1)])
    S1.send_message('Hello, World!')
    S1.send_message('Hello, Sx!', target='1111')

    print("服务器1 id：" + str(S1.ids))
    print("服务器2 id：" + str(S2.ids))
    print(S2.get_message())


if __name__ == '__main__':
    main()
