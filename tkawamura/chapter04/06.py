import matplotlib.pyplot as plt
import numpy as np

fs = 44100
fft_size = 65536
x = np.zeros((fft_size, 1))
x[1] = 1  # 教科書では2 (MATLAB)
X = np.fft.fft(x, fft_size, axis=0)
w = np.arange(fft_size).reshape(fft_size, 1) * fs / fft_size
phase_delay = -np.unwrap(np.angle(X[:, 0])) / (2 * np.pi * w[:, 0])
plt.plot(w, phase_delay * fs)
plt.xlabel("Frequency [Hz]")
plt.show()
