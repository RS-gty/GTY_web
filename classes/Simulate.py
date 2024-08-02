from utils.data_imports import *

from classes.Host import Host


class Simulate(object):
    def __init__(self):
        self.Atoms = []
        self.Hosts = []
        self.Servers = []

        self.frame = 0

    def new_host(self, name: str, pos: np.ndarray):
        g[name] = Host(pos)
        self.Hosts.append(name)

    def update(self):
        self.frame += 1
