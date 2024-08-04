from utils.data_imports import *

from classes.Signal import *


class Host(object):
    def __init__(self, pos: np.ndarray):
        self._position = pos
        self.__message = []
        self.id = ''.join(random.sample(string.ascii_letters, 4))
        self.atoms = []
        self.servers = []
        self.server_id = []
        self.public_key, self.__private_key = rsa.newkeys(1024)
        self.frame = 0

    def id_generator(self):
        s = ''.join(random.sample(string.ascii_letters, 8))
        while s not in self.server_id:
            return s

    def register(self, server):
        if True:
            server_id = self.id_generator()
            self.servers.append(server)
            self.server_id.append(server_id)
            return [server_id, True]

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
