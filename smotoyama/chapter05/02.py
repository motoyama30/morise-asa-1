import numpy as np
import matplotlib.pyplot as plt

fs = 8000
t = np.arange(fs) / fs
f1 = 3
f2 = 3.5
fft_size = 2 ** 17
w = np.arange(fft_size) / fft_size * fs

# cal
x1 = np.cos(2 * np.pi * f1 * t)
x2 = np.cos(2 * np.pi * f2 * t)
X1 = abs(np.fft.fft(x1, fft_size)) / len(x1)
X2 = abs(np.fft.fft(x2, fft_size)) / len(x2)

# plot
plt.subplot(2, 1, 1)
plt.stem(w, X1, ls="--")
plt.xlabel("周波数[Hz]")
plt.ylabel("振幅")
plt.xlim(0, 10)
plt.title("3Hz ")

plt.subplot(2, 1, 2)
plt.stem(w, X2, ls="--")
plt.xlabel("周波数[Hz]")
plt.ylabel("振幅")
plt.xlim(0, 10)
plt.title("3.5Hz ")

plt.tight_layout()
plt.show()
