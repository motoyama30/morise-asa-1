import numpy as np


# パラメータ
fs = 44100
N = 22050

x = np.random.randn(N)
energy = sum(x ** 2) / fs
x = x / np.sqrt(energy)
t = np.arange(0, len(x)) / fs
t_c = sum(t * x ** 2) / fs
sigma_t1 = sum((t - t_c) ** 2 * x ** 2) / fs

fft_size = int(2 ** np.ceil(np.log2(len(x))))
X = np.fft.fft(x, fft_size)
Xd = np.fft.fft(-1j * t * x, fft_size)
tau_d = (Xd.real * X.imag - X.real * Xd.imag) / abs(X) ** 2
d1 = ((X.real * Xd.real + X.imag * Xd.imag) / abs(X)) ** 2
d2 = (-tau_d + t_c) ** 2 * abs(X) ** 2
sigma_t2 = (sum(d1) + sum(d2)) / fft_size / fs

print(f"sigma_t1: {sigma_t1:.20f}")
print(f"sigma_t2: {sigma_t2:.20f}")
