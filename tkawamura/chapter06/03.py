import matplotlib.pyplot as plt
import numpy as np

N = 128

k = np.arange(N)
spec1 = np.abs(1 / (1 - 0.5 * np.exp(-1j * 2 * np.pi * k / N)))

h = np.zeros(N)
h[0] = 1
for n in range(1, N):
    h[n] = 0.5 * h[n - 1]

spec2 = np.abs(np.fft.fft(h))

plt.subplot(2, 1, 1)
plt.title("spec1")
plt.plot(k, spec1)
plt.xlim(0, N)
plt.xlabel("Discrete frequency number")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(2, 1, 2)
plt.title("spec2")
plt.plot(k, spec2)
plt.xlim(0, N)
plt.xlabel("Discrete frequency number")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
