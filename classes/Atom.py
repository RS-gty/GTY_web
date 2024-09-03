from utils.data_imports import *


from classes.Signal import *


class Atom(object):
    def __init__(self, host, radius: np.float64):
        self.__center = host.get_position()
        self.__radius = radius
        self.__signals = []
        self.__matrix = np.zeros((int(2 * radius + 1), int(2 * radius + 1)))
        self.__host = host
        self.frame = 0
        self.server_positions: list[list[str, np.ndarray]] = []

        host.atom = self

        ATOMS.append(self)

    def check(self, coordinate: np.ndarray) -> bool:
        if np.linalg.norm(coordinate - self.__center) <= self.__radius:
            return True
        else:
            return False

    def receive_signal(self, signal: Signal):
        self.__signals.append(signal)

    def update(self):
        for i in self.server_positions:
            density = 0
            for signal in self.__signals:
                if signal.is_accessible(i[1]):
                    try:
                        density += signal.density(signal.get_distance(i[1]))
                    except ValueError:
                        pass
            print(density)

    def get_matrix(self):
        return self.__matrix

    def get_radius(self):
        return self.__radius

    def sync(self, frame: int):
        self.frame = frame
