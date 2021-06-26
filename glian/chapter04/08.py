
import numpy as np

fs = 44100
N = 22050
x = np.random.randn(N)
energy = np.sum(x ** 2) / fs
x = x / np.sqrt(energy)
t = np.arange(x.shape[0]) / fs
t_c1 = np.sum(t * x ** 2) / fs

fft_size = 2 ** np.math.ceil(np.log2(x.shape[0]))
X = np.fft.fft(x, fft_size)
Xd = np.fft.fft(-1j * t * x, fft_size)
tau_d = (np.real(Xd) * np.imag(X) - np.real(X) * np.imag(Xd)) / np.abs(X) ** 2
t_c2 = np.sum(tau_d * np.abs(X) ** 2) / fs / fft_size

print(t_c1)
print(t_c2) # t_c1 = t_c2