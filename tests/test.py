
import numpy as np
import matplotlib.pyplot as plt
import time

lens = 5
num = 10000
t = np.linspace(0, lens, num)
x = np.cos(2 * np.pi * t + 0.5) + 0.1*np.cos(2 * np.pi * 100 * t)
X = np.fft.fft(x)
A = (X.real ** 2 + X.imag ** 2) ** 0.5 * 2 / num

k = np.fft.fftfreq(num, lens/num)

a = 1
tic = time.time()
while a <= 10000:
    a += 1
tac = time.time()
print(tac-tic)

PHI = np.angle(X)
plt.plot(x)
plt.plot(k, A)
plt.show()
