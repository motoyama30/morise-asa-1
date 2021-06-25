import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 44100
fft_size = 65536

x = np.zeros(fft_size)
x[1] = 1
X = np.fft.fft(x, fft_size)
w = np.arange(0, fft_size) / fft_size * fs
phase_delay = -np.unwrap(np.angle(X)) / (2 * np.pi * w)

# 結果
plt.plot(w, phase_delay * fs)
plt.xlabel("frequency [Hz]")
plt.ylabel("sample")
plt.grid()

plt.show()
