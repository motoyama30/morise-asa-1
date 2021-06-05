import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 44100
f = 5

t = np.arange(0, fs) / fs
x = np.sin(2 * np.pi * f * t)
fft_size = int(2 ** np.ceil(np.log2(len(x))))
X1 = np.fft.fft(x)
X2 = np.fft.fft(x, fft_size)

w = np.arange(0, fft_size) * fs / fft_size

# 結果
plt.plot(w, abs(X2))
plt.xlim(0, 50)
plt.xlabel("frequency [Hz]")
plt.ylabel("amplitude")
plt.grid()

plt.show()
