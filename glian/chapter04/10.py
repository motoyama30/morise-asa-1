import numpy as np

#スペクトル重心
fs = 44100
t = np.arange(fs) / fs
f = 1000
x = np.sin(2 * np.pi * f * t)
fft_size = 65536
X = np.fft.fft(x, fft_size)
X = np.abs(X[: fft_size // 2])
w = np.arange(fft_size // 2) / fft_size * fs

spectral_centroid = np.sum(w * X) / np.sum(X)
print("spectral_centroid [Hz]:{}".format(spectral_centroid))