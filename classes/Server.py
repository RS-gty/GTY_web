from utils.data_imports import *

from classes.Atom import Atom
from classes.Host import Host
from classes.Signal import *


class Server(object):
    def __init__(self, pos: np.ndarray):
        self.__position = pos
        self.__ids = []
        self.time = 0
        self.atoms: list[Atom] = []
        self.hosts = []
        self.public_key, self.__private_key = rsa.newkeys(1024)
        self.frame = 0

        for atom in ATOMS:
            if atom.check(self.__position):
                self.atoms.append(atom)

    def register(self, host: Host, server_id: str):
        self.hosts.append(host)
        self.__ids.append(server_id)

    def send_message(self, message, hosts=None, target=None, time: np.float16 = 0):
        if hosts is None:
            for host in self.hosts:
                temp_message = rsa.encrypt(message.encode('utf-8'), host.public_key)
                host.receive_message(self.__ids[self.hosts.index(host)], temp_message, target, time)
        else:
            for host in hosts:
                temp_message = rsa.encrypt(message.encode('utf-8'), host.public_key)
                host.receive_message(self.__ids[self.hosts.index(host)], temp_message, target, time)

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

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.__private_key

    def update(self):
        pass

    def get_position(self):
        return self.__position

    def sync(self, frame: int):
        self.frame = frame
