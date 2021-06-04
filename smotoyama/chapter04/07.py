import numpy as np
import matplotlib.pyplot as plt

fs = 44100
fft_size = 65536
x = np.zeros(fft_size)
x[1] = 1
t = np.arange(len(x))
w = np.arange(fft_size) / fft_size * fs

X = np.fft.fft(x, fft_size)
Xd = np.fft.fft(-1j * t, x, fft_size)
tau_d = (np.real(Xd) * np.imag(X) - np.real(X) * np.imag(Xd)) / abs(X) ** 2

plt.plot(w, tau_d)
plt.ylabel("遅延")
plt.xlabel("周波数[Hz]")
plt.grid()
