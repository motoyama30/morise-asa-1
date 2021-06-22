import numpy as np
import matplotlib.pyplot as plt

fs = 44100
len_t = 1
t = np.arange(fs * len_t) / fs
f = 5
x = np.sin(2 * np.pi * f * t)
fft_size = int(2 ** np.ceil(np.log2(len(t))))
X1 = np.fft.fft(x)
X2 = np.fft.fft(x, fft_size)

print(f"{np.sum(x**2):.2f}")
print(f"{np.sum(np.abs(X1)**2)/len(X1):.2f}")
print(f"{np.sum(np.abs(X2)**2)/fft_size:.2f}")
