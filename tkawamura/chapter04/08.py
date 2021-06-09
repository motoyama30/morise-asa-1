import matplotlib.pyplot as plt
import numpy as np

fs = 44100
N = 22050
x = np.random.randn(N, 1)
energy = np.sum(x ** 2) / fs
x = x / np.sqrt(energy)
t = np.arange(len(x)).reshape((len(x), 1)) / fs
t_c1 = np.sum(t * x ** 2) / fs

fft_size = int(2 ** np.ceil(np.log2(len(x))))
X = np.fft.fft(x, fft_size, axis=0)
Xd = np.fft.fft(-1j * t * x, fft_size, axis=0)
tau_d = (Xd.real * X.imag - X.real * Xd.imag) / np.abs(X) ** 2
t_c2 = np.sum(tau_d * np.abs(X) ** 2) / fs / fft_size

print(f"{t_c1:.20f}")
print(f"{t_c2:.20f}")
