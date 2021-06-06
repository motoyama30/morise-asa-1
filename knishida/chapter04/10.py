import numpy as np


# declare
fs = 44100
t = np.arange(0, 1, 1 / fs)
f = 1000
x = np.sin(2 * np.pi * f * t)
fft_size = 65536

# calc
X = np.fft.fft(x, fft_size)
X = np.abs(X[0 : int(fft_size / 2 + 1)])
w = np.arange(0, fft_size / 2 + 1) * fs / fft_size
spectral_centroid = np.sum(w * X) / np.sum(X)

# output
print(spectral_centroid)
