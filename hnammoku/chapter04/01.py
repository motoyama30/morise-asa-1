# 正弦波のスペクトル解析
import matplotlib.pyplot as plt
import numpy as np

# 信号の生成
fs = 44100
t = np.arange(fs * 2) / fs
f = 5
x = np.sin(2 * np.pi * f * t)
X = np.fft.fft(x, axis=0)

# 振幅スペクトルの表示
w = np.arange(len(x)).T * fs / len(x)
plt.plot(w, np.abs(X))
plt.title("Amplitude spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.xlim(0, 50)
plt.show()
