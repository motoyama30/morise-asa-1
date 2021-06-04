# ゼロ埋めによる信号長の調整
import numpy as np
import matplotlib.pyplot as plt

# 信号生成
fs = 44100
t = np.arange(fs) / fs
f = 5
x = np.sin(2 * np.pi * f * t)
fft_size = 2 ** np.ceil(np.log2(len(x)))
X1 = np.fft.fft(x, axis=0)
X2 = np.fft.fft(x, int(fft_size), axis=0)

# 振幅スペクトル表示
w = np.arange(fft_size).T * fs / fft_size
plt.plot(w, np.abs(X2))
plt.title("Amplitude spectrum for a zero-padded signal")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.xlim(0, 50)
plt.show()
