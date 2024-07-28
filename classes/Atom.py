from utils.data_imports import *

from classes.Host import Host
from classes.Signal import *


class Atom(object):
    def __init__(self, host: Host, radius: np.float64):
        self.__center = host.get_position()
        self.__radius = radius
        self.__signals = []

        ATOMS.append(self)

    def check(self, coordinate: np.ndarray) -> bool:
        if np.linalg.norm(coordinate - self.__center) <= self.__radius:
            return True
        else:
            return False

    def receive_signal(self, signal: Signal):
        self.__signals.append(signal)
