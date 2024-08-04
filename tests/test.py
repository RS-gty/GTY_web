
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

R = np.random.randn(19, 19)


print(np.modf(21.35124)[0])
PHI = np.angle(X)
plt.plot(x)
plt.plot(k, A)
plt.show()