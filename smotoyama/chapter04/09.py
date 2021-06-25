import numpy as np

fs = 44100
N = 22050
x = np.random.randn(N)
energy = sum(x ** 2) / fs
x = x / np.sqrt(energy)
t = np.arange(len(x)) / fs
t_c = sum(t * x ** 2) / fs
fft_size = 2 ** np.ceil(np.log2(len(x)))
sigma_t1 = np.sum((t - t_c) ** 2 * x ** 2) / fs

X = np.fft.fft(x, int(fft_size))
Xd = np.fft.fft(-1j * t * x, int(fft_size))
tau_d = (np.real(Xd * np.imag(X) - np.real(X) * np.imag(Xd))) / abs(X) ** 2
d1 = ((np.real(X) * np.real(Xd) + np.imag(X) * np.imag(Xd)) / abs(X)) ** 2
d2 = (-tau_d + t_c) ** 2 * abs(X) ** 2
sigma_t2 = (np.sum(d1) + sum(d2)) / fft_size / fs

print(sigma_t1)
print(sigma_t2)
