import numpy as np
import matplotlib.pyplot as plt

fs = 44100
fft_size = 65536
x = np.zeros(fft_size)
x[1] = 1
X = np.fft.fft(x, fft_size)
w = np.arange(fft_size) / fft_size * fs #横軸を周波数に変更
phase_delay = -np.unwrap(np.angle(X)) / (2 * np.pi * w)
plt.plot(w, phase_delay * fs)
plt.xlabel("frequency [Hz]")
plt.ylabel("sample")
plt.grid()
plt.tight_layout()
plt.show()
