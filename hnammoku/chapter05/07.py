# チャープ信号の生成とスペクトル解析
import numpy as np
import matplotlib.pyplot as plt

# 信号生成
fs = 8000
T = 1
f1 = 100
f2 = 2000
k = (f2 - f1) / T
t = np.arange(fs * T) / fs
x = np.sin(2 * np.pi * (f1 * t + (k / 2) * t ** 2))

# パワースペクトル算出
fft_size = 8000
w = np.arange(fft_size) / fft_size * fs
plt.plot(w, 20 * np.log10(np.abs(np.fft.fft(x, fft_size))))
plt.xlim(0, 3000)
plt.title("Power spectrum of chirp signal")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Power [dB]")
plt.show()
