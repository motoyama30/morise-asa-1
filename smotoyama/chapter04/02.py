import numpy as np
import matplotlib.pyplot as plt

fs = 44100
t = np.arange(fs * 2) / fs
f = 5
x = np.sin(2 * np.pi * f * t)
fft_size = 2 ** np.ceil(np.log2(len(x)))

# cul
X1 = np.fft.fft(x)
X2 = np.fft.fft(x, int(fft_size))
w = np.arange(fft_size) * fs / fft_size

# plot
plt.plot(w, abs(X2))
plt.xlabel("周波数[Hz]")
plt.ylabel("振幅")
plt.grid()
plt.xlim(0, 50)
