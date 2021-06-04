import numpy as np
import matplotlib.pyplot as plt

fs = 44100
fft_size = 65536
x = np.zeros(fft_size)
x[1] = 1
w = np.arange(fft_size) / fft_size * fs

X = np.fft.fft(x, fft_size)
phase_delay = -np.unwrap(np.angle(X)) / (2 * np.pi * w)

plt.plot(w, phase_delay * fs)
plt.ylabel("サンプル")
plt.xlabel("周波数[Hz]")
plt.grid()
