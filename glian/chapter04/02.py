import numpy as np
import matplotlib.pyplot as plt

"""
2のべき乗の信号長まで0埋め
"""
fs = 44100
len_t = 1
t = np.arange(fs * len_t) / fs
f = 5
x = np.sin(2 * np.pi * f * t)
fft_size = int(2 ** np.ceil(np.log2(len(t))))
X2 = np.fft.fft(x, fft_size)

w = np.arange(fft_size) / fft_size * fs  # 横軸をもともとの周波数番号から、真の周波数[Hz]に変換
plt.plot(w, np.abs(X2))
plt.xlim(0, 50)
plt.show()
