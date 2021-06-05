import numpy as np
import matplotlib.pyplot as plt


# declare
fs = 44100
fft_size = 65536
x = np.zeros(fft_size)
x[1] = 1
w = np.arange(0, fft_size) / fft_size * fs

# calc
X = np.fft.fft(x, fft_size)
phase_delay = -np.unwrap(np.angle(X)) / (2 * np.pi * w)

# output
plt.plot(w, phase_delay * fs)
plt.xlabel("frequency [Hz]")
plt.ylabel("Sample")
plt.show()
