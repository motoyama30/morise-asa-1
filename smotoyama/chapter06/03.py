import numpy as np
import matplotlib.pyplot as plt

N = 128
k = np.arange(N)
spec1 = abs(1 / (1 - 0.5 * np.exp(-1j * 2 * np.pi * k / N)))
h = np.zeros(N)
h[0] = 1
for n in range(1, N):
    h[n] = 0.5 * h[n - 1]

spec2 = abs(np.fft.fft(h))

plt.subplot(2, 1, 1)
plt.plot(k, spec1)
plt.title("spec1")
plt.xlabel("k")
plt.ylabel("amplitude")
plt.xlim(0, N - 1)

plt.subplot(2, 1, 2)
plt.plot(k, spec2)
plt.title("spec2")
plt.xlabel("k")
plt.ylabel("amplitude")
plt.xlim(0, N - 1)

plt.tight_layout()
plt.show()
