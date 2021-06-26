import matplotlib.pyplot as plt
import numpy as np

fs = 8000
T = 1
f1 = 100
f2 = 2000
k = (f2 - f1) / T
t = np.arange(fs * T) / fs
x = np.sin(2 * np.pi * (f1 * t + (k / 2) * t ** 2))

fft_size = 8000
w = np.arange(fft_size) * fs / fft_size
plt.plot(w, 20 * np.log10(np.abs(np.fft.fft(x, fft_size))))
plt.xlabel("Frequency [Hz]")
plt.ylabel("Relative power [dB]")
plt.xlim(0, 3000)
plt.ylim(-10, 50)
plt.grid()
plt.show()
