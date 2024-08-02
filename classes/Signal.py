from utils.imports import *


class Signal(object):
    def __init__(self, center: np.ndarray, content: str or bytes, strength, frequency,
                 direction=None, concentrate=np.pi):

        self.__center = center
        self.content: str or bytes = content
        self.__strength = strength
        self.__frequency = frequency
        self.__dir = direction
        self.__concentrate = 0

        if self.__dir is not None:
            self.__concentrate = concentrate
        else:
            if concentrate == np.pi:
                self.__concentrate = concentrate
            else:
                raise ValueError("'value:concentrate' must be set after the direction is defined")

    def encrypt(self, pub_key):
        self.content = rsa.encrypt(self.content.encode("utf-8"), pub_key)
        return self

    def decrypt(self, pri_key):
        self.content = rsa.decrypt(self.content, pri_key).decode("utf-8")
        return self

    def density(self, distance):
        return self.__strength / (2 * np.pi * (1 - np.cos(self.__concentrate)) * distance ** 2)

    def is_accessible(self, target: np.ndarray) -> bool:
        target_vector = target - self.__center
        if self.__dir is None:
            if self.density(np.linalg.norm(target_vector)) > 1:
                return True
            else:
                return False
        else:
            if (self.density(np.linalg.norm(target_vector)) > 1 and
                    np.arccos(np.dot(target_vector, self.__dir) /
                              (np.linalg.norm(target_vector) * np.linalg.norm(self.__dir))) <= self.__concentrate):
                return True
            else:
                return False
