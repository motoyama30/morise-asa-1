import matplotlib.pyplot as plt
import numpy as np

fs = 44100
t = np.arange(fs).reshape(fs, 1) / fs  # 信号長が1秒分
f = 5
x = np.sin(2 * np.pi * f * t)
fft_size = int(2 ** np.ceil(np.log2(len(x))))  # int型へキャスティング
X2 = np.fft.fft(x, fft_size, axis=0)

w = np.arange(fft_size) * fs / fft_size

plt.plot(w, np.abs(X2))
plt.xlim(0, 50)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.show()
