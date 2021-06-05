import numpy as np


# パラメータ
fs = 44100
N = 22050

x = np.random.randn(N)
energy = sum(x ** 2) / fs
x = x / np.sqrt(energy)
t = np.arange(0, len(x)) / fs
t_c1 = sum(t * x ** 2) / fs

fft_size = int(2 ** np.ceil(np.log2(len(x))))
X = np.fft.fft(x, fft_size)
Xd = np.fft.fft(-1j * t * x, fft_size)
tau_d = (Xd.real * X.imag - X.real * Xd.imag) / abs(X) ** 2
t_c2 = sum(tau_d * abs(X) ** 2) / fs / fft_size

print(f"t_c1: {t_c1:.20f}")
print(f"t_c2: {t_c2:.20f}")
