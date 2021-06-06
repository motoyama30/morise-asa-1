import numpy as np

fs = 44100
t = np.arange(fs) / fs
f = 1000
x = np.sin(2 * np.pi * f * t)
fft_size = 65536

X = np.fft.fft(x, fft_size)
X = abs(X[0 : int(fft_size / 2) + 1])
w = np.arange(fft_size / 2) * fs / fft_size
spectral_centroid = np.sum(w * X) / np.sum(X)

print(spectral_centroid)
