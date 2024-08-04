from utils.data_imports import *

from classes.Signal import Signal
from classes.Host import Host
from classes.Atom import Atom
from classes.Server import Server


class Simulate(object):
    def __init__(self):
        self.frame = 0
        self.Atoms: list[Atom] = []
        self.Hosts: list[Host] = []
        self.Servers: list[Server] = []

        self.Signals: list[Signal] = []
        for s in self.Signals:
            s.set_origin_frame(self.frame)

    def new_host(self, name: str, pos: np.ndarray):
        g[name] = Host(pos)
        self.Hosts.append(name)

    def update(self):
        self.frame += 1
        for s in self.Servers:
            s.sync(self.frame)
        for i in self.Atoms + self.Hosts + self.Servers:
            i.update()
            i.sync(self.frame)
