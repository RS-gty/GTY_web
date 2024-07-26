import string

import numpy as np
import random

ATOMS = []


class Atom(object):
    def __init__(self, cen: np.ndarray, r):
        self.__center = cen
        self.__radius = r
        ATOMS.append(self)

    def check(self, coordinate: np.ndarray) -> bool:
        if np.linalg.norm(coordinate - self.__center) <= self.__radius:
            return True
        else:
            return False


class Host(object):
    def __init__(self, pos: np.ndarray):
        self.position = pos
        self.id = ''.join(random.sample(string.ascii_letters, 4))
        self.atoms = []
        self.servers = []
        self.server_id = []
        self.time = 0
        self.__message = []

    def update(self):
        self.time += 1

    def id_generator(self):
        s = ''.join(random.sample(string.ascii_letters, 8))
        while s not in self.server_id:
            return s

    def receive_message(self, server_id, message, target, time):
        self.__message.append([message, server_id, target, time])

    def deliver_message(self, server_id):
        messages = []
        for message in self.__message:
            if message[2] is None or message[2] == server_id:
                messages.append(message[0])
        return messages


class Server(object):
    def __init__(self, pos: np.ndarray):
        self.position = pos
        self.time = 0
        self.atoms = []
        self.hosts = []
        self.__ids = []

    def initialize(self):
        for atom in ATOMS:
            if atom.check(self.position):
                self.atoms.append(atom)

    def register(self, host: Host):
        server_id = host.id_generator()
        host.servers.append(self)
        host.server_id.append(server_id)
        self.hosts.append(host)
        self.__ids.append(server_id)

    def send_message(self, message, hosts=None, target=None, time: np.float16 = 0):
        if hosts is None:
            for host in self.hosts:
                host.receive_message(self.__ids[self.hosts.index(host)], message, target, time)
        else:
            for host in hosts:
                host.receive_message(self.__ids[self.hosts.index(host)], message, target, time)

    def send_command(self, command: str, target: Host = None, time: np.float16 = 0):
        pass

    def get_message(self, hosts=None):
        messages = []
        if hosts is None:
            for host in self.hosts:
                messages.append(host.deliver_message(self.__ids[self.hosts.index(host)]))
        else:
            for host in self.hosts:
                messages.append(host.deliver_message(self.__ids[self.hosts.index(host)]))
        return messages

    def get_id(self, hosts=None):
        if hosts is None:
            return self.__ids
        else:
            return self.__ids[self.hosts.index(hosts)]


def main():
    A1 = Atom(np.array([0, 0, 0]), 10)

    H1 = Host(np.array([0, 0, 0]))
    H2 = Host(np.array([0, 0, 1]))

    S1 = Server(np.array([2, 1, 0]))
    S2 = Server(np.array([-4, 3, 0]))

    S1.initialize()
    print(S1.atoms)

    S1.register(H1)
    S2.register(H1)

    S1.send_message('S1_id:' + S1.get_id()[0])
    S1.send_message('Hello, World!', time=np.float64(2))

    print("服务器1 id：" + str(S1.get_id()))
    print("服务器2 id：" + str(S2.get_id()))
    print(S2.get_message())


if __name__ == '__main__':
    main()
