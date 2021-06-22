import numpy as np
import matplotlib.pyplot as plt

fs = 44100
len_t = 2
t = np.arange(fs * len_t) / fs
f = 5
x = np.sin(2 * np.pi * f * t)
X = np.fft.fft(x)  # fs*len_t = 88200点= len(t)
# plt.plot(t, x)
# その88200点で標本化周期44100を分割する
w = np.arange(len(t)) / len(t) * fs  # 横軸をもともとの周波数番号から、真の周波数[Hz]に変換
plt.plot(w, np.abs(X))
plt.xlim(0, 50)
plt.show()
