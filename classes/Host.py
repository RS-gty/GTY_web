from utils.data_imports import *

from classes.Signal import *
from classes.Atom import *


class Host(object):
    def __init__(self, pos: np.ndarray):
        self._position = pos
        self.__message = []
        self.id = ''.join(random.sample(string.ascii_letters, 4))
        self.atom: Atom or None = None
        self.servers = []
        self.server_id = []
        self.public_key, self.__private_key = rsa.newkeys(1024)
        self.frame = 0

    def id_generator(self):
        s = ''.join(random.sample(string.ascii_letters, 8))
        while s not in self.server_id:
            return s

    def register(self, *servers):
        for server in servers:
            if np.linalg.norm(server.get_position() - self._position) <= self.atom.get_radius() and server not in self.servers:
                server_id = self.id_generator()
                self.servers.append(server)
                self.server_id.append(server_id)
                self.atom.server_positions.append([server_id, server.get_position()])
                server.register(self, server_id)
            else:
                pass

    def get_position(self):
        return self._position

    def receive_message(self, server_id, message, target, time):
        self.__message.append([message, server_id, target, time])

    def deliver_message(self, server_id):
        messages = []
        for message in self.__message:
            if message[2] is None or message[2] == server_id:
                messages.append(message[0])
        return messages

    def update(self):
        pass

    def sync(self, frame: int):
        self.frame = frame
