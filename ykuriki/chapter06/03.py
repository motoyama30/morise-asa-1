import numpy as np
import matplotlib.pyplot as plt


# パラメータ
N = 128

k = np.arange(0, N)
spec1 = abs(1 / (1 - 0.5 * np.exp(-1j * 2 * np.pi * k / N)))

h = np.zeros(N)
h[0] = 1
for n in range(1, N):
    h[n] = 0.5 * h[n - 1]
spec2 = abs(np.fft.fft(h))

# プロット
fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(k, spec1)
ax1.set_xlim(0, N - 1)
ax1.set_xlabel("k")
ax1.set_ylabel("amplitude")
ax1.set_title("spec1")
ax1.grid()

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(k, spec2)
ax2.set_xlim(0, N - 1)
ax2.set_xlabel("k")
ax2.set_ylabel("amplitude")
ax2.set_title("spec2")
ax2.grid()

plt.tight_layout()

plt.show()
