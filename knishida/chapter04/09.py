import numpy as np


# declare
fs = 44100
N = 22050
x = np.random.randn(N)
energy = np.sum(x ** 2) / fs
x = x / np.sqrt(energy)
t = np.arange(0, len(x)) / fs
t_c = np.sum(t * x ** 2) / fs
sigma_t1 = np.sum((t - t_c) ** 2 * x ** 2) / fs

# calc
fft_size = 2 ** np.ceil(np.log2(len(x)))
X = np.fft.fft(x, int(fft_size))
Xd = np.fft.fft(-1j * t * x, int(fft_size))
tau_d = (np.real(Xd) * np.imag(X) - np.real(X) * np.imag(Xd)) / np.abs(X) ** 2
d1 = ((np.real(X) * np.real(Xd) + np.imag(X) * np.imag(Xd)) / np.abs(X)) ** 2
d2 = (-tau_d + t_c) ** 2 * np.abs(X) ** 2
sigma_t2 = (np.sum(d1) + np.sum(d2)) / fft_size / fs

# output
print("{:.20f}".format(sigma_t1))
print("{:.20f}".format(sigma_t2))
