import time

import rsa

from utils.imports import *
from utils.class_imports import *


def main():
    H1 = Host(np.array([0, 0, 0]))
    H2 = Host(np.array([0, 0, 1]))

    A1 = Atom(H1, np.float64(10))

    S1 = Server(np.array([2, 1, 0]))
    S2 = Server(np.array([-4, 3, 0]))

    print(S1.atoms)

    S1.register(H1)
    S2.register(H1)

    S1.send_message('S1_id:' + S1.get_id()[0])
    S1.send_message('Hello, World!', time=np.float64(2))

    print("服务器1 id：" + str(S1.get_id()))
    print("服务器2 id：" + str(S2.get_id()))
    print(S1.get_message())

    Sig1 = Signal(np.array([0, 0, 0]), "RSgty", 100, np.array([0, 1, 0]), np.pi/4)

    A1.receive_signal(Sig1)
    A1.update()

    M = A1.get_matrix()


if __name__ == '__main__':
    H1 = Host(np.array([0, 0, 0]))
    H2 = Host(np.array([0, 0, 1]))

    A1 = Atom(H1, np.float64(10))

    S1 = Server(np.array([2, 1, 0]))
    S2 = Server(np.array([-4, 3, 0]))

    print(S1.atoms)

    S1.register(H1)
    S2.register(H1)

    S1.send_message('S1_id:' + S1.get_id()[0])
    S1.send_message('Hello, World!', time=np.float64(2))

    print("服务器1 id：" + str(S1.get_id()))
    print("服务器2 id：" + str(S2.get_id()))
    print(S1.get_message())

    Sig1 = Signal(np.array([0, 0, 0]), "RSgty", 10000, frequency=10, direction=np.array([0, 1, 0]), concentrate=np.pi / 4)

    A1.receive_signal(Sig1)
    A1.update()

    M = A1.get_matrix()
    M[2, 3] += 114
    print(M)

