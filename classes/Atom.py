import string
import numpy as np
import random

from utils.data_imports import *
from classes.Host import Host


class Atom(object):
    def __init__(self, host: Host, radius: np.float64):
        self.__center = host.get_position()
        self.__radius = radius
        ATOMS.append(self)

    def check(self, coordinate: np.ndarray) -> bool:
        if np.linalg.norm(coordinate - self.__center) <= self.__radius:
            return True
        else:
            return False
