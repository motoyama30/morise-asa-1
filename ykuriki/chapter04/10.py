import numpy as np


# パラメータ
fs = 44100
f = 1000
fft_size = 65536

t = np.arange(0, fs) / fs
x = np.sin(2 * np.pi * f * t)
X = np.fft.fft(x, fft_size)
X = abs(X[0 : fft_size // 2 + 1])
w = np.arange(0, fft_size / 2 + 1) * fs / fft_size
spectal_centroid = sum(w * X) / sum(X)

print(spectal_centroid)
