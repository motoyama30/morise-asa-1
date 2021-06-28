import numpy as np
import matplotlib.pyplot as plt

fs = 8000
T = 1
f1 = 100
f2 = 2000
k = (f2 - f1) / T
t = np.arange(fs * T) / fs
fft_size = 8000
w = np.arange(fft_size) / fft_size * fs

x = np.sin(2 * np.pi * (f1 * t + (k / 2) * t ** 2))

plt.plot(w, 20 * np.log10(abs(np.fft.fft(x, fft_size))))
plt.xlim(0, 3000)
plt.xlabel("周波数[Hz]")
plt.ylabel("相対パワー[dB]")
plt.show()
