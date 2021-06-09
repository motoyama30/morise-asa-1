import matplotlib.pyplot as plt
import numpy as np

fs = 44100
N = 22050

x = np.random.randn(N, 1)
fft_size = int(2 ** np.ceil(np.log2(len(x))))
energy = np.sum(x ** 2) / fft_size
x = x / np.sqrt(energy)
t = np.arange(len(x)).reshape((len(x), 1)) / fs
t_c = np.sum(t * x ** 2) / fs
sigma_t1 = np.sum((t - t_c) ** 2 * x ** 2) / fs

fft_size = int(2 ** np.ceil(np.log2(len(x))))
X = np.fft.fft(x, fft_size, axis=0)
Xd = np.fft.fft(-1j * t * x, fft_size, axis=0)
tau_d = (Xd.real * X.imag - X.real * Xd.imag) / np.abs(X) ** 2

d1 = ((X.real * Xd.real + X.imag * Xd.imag) / np.abs(X)) ** 2
d2 = (-tau_d + t_c) ** 2 * np.abs(X) ** 2

sigma_t2 = (np.sum(d1) + np.sum(d2)) / fft_size / fs

print(f"{sigma_t1:.20f}")
print(f"{sigma_t2:.20f}")
