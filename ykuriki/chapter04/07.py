import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 44100
fft_size = 65536

x = np.zeros(fft_size)
x[1] = 1
t = np.arange(0, len(x))
X = np.fft.fft(x, fft_size)
Xd = np.fft.fft(-1j * t * x, fft_size)
tau_d = (Xd.real * X.imag - X.real * Xd.imag) / abs(X) ** 2

w = np.arange(0, fft_size) / fft_size * fs

# 結果
plt.plot(w, tau_d)
plt.xlabel("frequency [Hz]")
plt.ylabel("delay")
plt.grid()

plt.show()
