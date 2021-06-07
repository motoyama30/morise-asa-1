import numpy as np
import matplotlib.pyplot as plt

N = 8
x = np.random.randn(N, 1)
c = np.zeros((N, 1), dtype=complex)
for i in range(N):
    c[i] = np.sum(x * np.exp(-1j * 2 * np.pi * i * np.arange(N) / N))

X = np.fft.fft(x)

print("error: {}".format(np.sum((c - X) ** 2)))

plt.plot(np.abs(c), label="c")
plt.plot(np.abs(X), label="X")
plt.legend()
plt.show()
