from utils.imports import *
from data.data import *


class Signal(object):
    def __init__(self, center: np.ndarray, content: str or bytes, strength, frequency,
                 direction=None, concentrate=np.pi):
        self.__center = center
        self.content: str or bytes = content
        self.__strength = strength
        self.__frequency = frequency
        self.__dir = direction
        self.__concentrate = 0
        self.__origin_frame = 0
        self.frame = 0

        if self.__dir is not None:
            self.__concentrate = concentrate
        else:
            if concentrate == np.pi:
                self.__concentrate = concentrate
            else:
                raise ValueError("'value:concentrate' must be set after the direction is defined")

    def sync(self, frame: int):
        self.frame = frame

    def set_origin_frame(self, origin: int):
        self.__origin_frame = origin

    def encrypt(self, pub_key):
        self.content = rsa.encrypt(self.content.encode("utf-8"), pub_key)
        return self

    def decrypt(self, pri_key):
        self.content = rsa.decrypt(self.content, pri_key).decode("utf-8")
        return self

    def get_distance(self, target: np.ndarray):
        return np.linalg.norm(self.__center - target)

    def density(self, distance):
        bias = 2*np.pi*(self.__frequency * (((self.frame - self.__origin_frame) / FPU) / UPS))
        amp = self.__strength / (2 * np.pi * (1 - np.cos(self.__concentrate)) * distance ** 2)
        n = np.sin(2 * np.pi * distance / (C / self.__frequency) + bias)
        return n * amp

    def is_accessible(self, target: np.ndarray) -> bool:
        target_vector = target - self.__center
        if self.__dir is None:
            return True
        else:
            if np.arccos(np.dot(target_vector, self.__dir)/(np.linalg.norm(target_vector) * np.linalg.norm(self.__dir))) <= self.__concentrate\
                    and np.linalg.norm(target_vector) <= C * (((self.frame - self.__origin_frame) / FPU) / UPS):
                return True
            else:
                return False
