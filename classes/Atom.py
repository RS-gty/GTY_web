from utils.data_imports import *

from classes.Host import Host
from classes.Signal import *


class Atom(object):
    def __init__(self, host: Host, radius: np.float64):
        self.__center = host.get_position()
        self.__radius = radius
        self.__signals = []
        self.__matrix = np.zeros((int(2 * np.ceil(radius) + 1), int(2 * np.ceil(radius) + 1)))

        ATOMS.append(self)

    def check(self, coordinate: np.ndarray) -> bool:
        if np.linalg.norm(coordinate - self.__center) <= self.__radius:
            return True
        else:
            return False

    def receive_signal(self, signal: Signal):
        self.__signals.append(signal)

    def update(self):
        for i in range(int(2 * np.ceil(self.__radius)) + 1):
            for j in range(int(2 * np.ceil(self.__radius)) + 1):
                for signal in self.__signals:
                    if signal.is_accessible(np.array([i - np.ceil(self.__radius), j - np.ceil(self.__radius), 0])):
                        try:
                            self.__matrix[i, j] += signal.density(signal.get_distance(np.array([i - np.ceil(self.__radius), j - np.ceil(self.__radius), 0])))
                        except ValueError:
                            pass

    def get_matrix(self):
        return self.__matrix
