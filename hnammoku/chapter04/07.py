# 群遅延の計算
import numpy as np
import matplotlib.pyplot as plt

# 信号生成
fs = 44100
fft_size = 65536
x = np.zeros(fft_size)
x[1] = 1
t = np.arange(len(x))
X = np.fft.fft(x, int(fft_size), axis=0)
Xd = np.fft.fft(-1j * t * x, int(fft_size), axis=0)
tau_d = (np.real(Xd) * np.imag(X) - np.real(X) * np.imag(Xd)) / np.abs(X) ** 2

w = np.arange(fft_size).T / fft_size * fs
plt.plot(w, tau_d)
plt.title("Group delay")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Delay [sample]")
plt.show()
