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

    A1 = Atom(H1, np.float64(2))

    Sig1 = Signal(np.array([0, 0, 0]), "RSgty", 1000, 0.70)
    Sig2 = Signal(np.array([0, 1, 0]), "RSgty", 2000, 0.47)
    A1.receive_signal(Sig1)
    A1.receive_signal(Sig2)

    Ser1 = Server(np.array([1, -1, 0]))
    Ser2 = Server(np.array([1, 1, 0]))
    """
    fig, ax = plt.subplots()
    imgs = []
    fig = plt.figure()
    y = []

    for step in tqdm.tqdm(range(100)):
        Sig1.frame = step
        A1.update()
        img = A1.get_matrix()
        im = plt.imshow(img, animated=True, cmap="Spectral", vmin=-100, vmax=100)
        imgs.append([im])
        y.append(A1.get_matrix()[0, 23])

    ani = animation.ArtistAnimation(fig, imgs, interval=0.2, repeat_delay=0)
    plt.show()
    print(1)
    """
    H1.register(Ser1)
    Y = []

    for frames in tqdm.tqdm(range(10000)):
        Sig1.frame = frames
        Sig2.frame = frames
        Y.append(A1.get_info(Ser1.get_id(H1)))
        A1.update()

    X = np.fft.fft(Y)
    A = (X.real ** 2 + X.imag ** 2) ** 0.5 * 2 / 10000
    k = np.fft.fftfreq(10000, 1)
    plt.plot(k, A)
    plt.show()
