import numpy as np
import matplotlib.pyplot as plt


# declare
fs = 44100
fft_size = 65536
x = np.zeros(fft_size)
x[1] = 1
t = np.arange(0, len(x))

# calc
X = np.fft.fft(x, fft_size)
Xd = np.fft.fft(-1j * t * x, fft_size)
tau_d = (np.real(Xd) * np.imag(X) - np.real(X) * np.imag(Xd)) / np.abs(X) ** 2

# output
w = np.arange(0, fft_size) / fft_size * fs
plt.plot(w, tau_d)
plt.xlabel("frequency [Hz]")
plt.ylabel("delay")
plt.show()
