import matplotlib.pyplot as plt
import numpy as np

fs = 44100
fft_size = 65536
x = np.zeros((fft_size, 1))
x[1] = 1  # 教科書では2 (MATLAB)
t = np.arange(len(x)).reshape((len(x), 1))
X = np.fft.fft(x, fft_size, axis=0)
Xd = np.fft.fft(-1j * t * x, fft_size, axis=0)  # 微分されたX
tau_d = (Xd.real * X.imag - X.real * Xd.imag) / np.abs(X) ** 2

w = np.arange(fft_size).reshape(fft_size, 1) * fs / fft_size
plt.plot(w, tau_d)
plt.xlabel("Frequency [Hz]")
plt.show()
