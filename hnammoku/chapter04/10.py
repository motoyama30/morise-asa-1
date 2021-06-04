# スペクトル重心の計算
import numpy as np

# 信号生成
fs = 44100
t = np.arange(fs) / fs
f = 1000
x = np.sin(2 * np.pi * f * t)
fft_size = 65536
X = np.fft.fft(x, int(fft_size), axis=0)
X = np.abs(X[0 : fft_size // 2])

w = np.arange(fft_size // 2).T * fs / fft_size
spectral_centroid = np.sum(w * X) / np.sum(X)
print(f"スペクトル重心：{spectral_centroid:.2f}")
