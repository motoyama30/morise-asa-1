import numpy as np
import matplotlib.pyplot as plt


# declare
fs = 8000
T = 1
f1 = 100
f2 = 2000
fft_size = 8000
k = (f2 - f1) / T
t = np.arange(0, T, 1 / fs)

# calc
x = np.sin(2 * np.pi * (f1 * t + (k / 2) * t ** 2))
w = np.arange(0, fft_size) / fft_size * fs

# output
plt.plot(w, 20 * np.log10(np.abs(np.fft.fft(x, fft_size))))
plt.xlim(0, 3000)
plt.xlabel("frequency (Hz)")
plt.ylabel("power (dB)")
plt.show()
