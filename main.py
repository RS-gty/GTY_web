from utils.imports import *
from utils.class_imports import *


def main():
    H1 = Host(np.array([0, 0, 0]))
    H2 = Host(np.array([0, 0, 1]))

    A1 = Atom(H1, np.float64(20))

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

    A1 = Atom(H1, np.float64(20))
    """
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
    """

    Sig1 = Signal(np.array([3, 0, 0]), "RSgty", 10000, 10, direction=np.array([0, 1, 0]), concentrate=np.pi/2)
    Sig2 = Signal(np.array([-3, 0, 0]), "RSgty", 10000, 10, direction=np.array([0, 1, 0]), concentrate=np.pi/2)
    Sig3 = Signal(np.array([0, 0, 0]), "RSgty", 10000, 10)
    Sig3.frame = 250

    A1.receive_signal(Sig3)



    tic = time.time()
    A1.update()
    tac = time.time()
    print(tac - tic)

    fig, ax = plt.subplots()
    imgs = []
    fig = plt.figure()

    for step in tqdm.tqdm(range(100)):
        Sig3.frame = step*10
        A1.update()
        img = A1.get_matrix()
        im = plt.imshow(img, animated=True, cmap="plasma", vmin=-10, vmax=10)
        imgs.append([im])

    ani = animation.ArtistAnimation(fig, imgs, interval=1, repeat_delay=0)
    plt.show()

