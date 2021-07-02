import numpy as np
import matplotlib.pyplot as plt

fs = 44100
fft_size = 65536

w = np.arange(0, fft_size) / fft_size * fs

plt.plot(w / 1000, abs(np.fft.fft(np.array([0.5, -0.5]), fft_size)))
plt.xlim(0, fs / 2000)
plt.grid()
plt.xlabel("Frequency [kHz]")
plt.ylabel("Amplitude")

plt.show()
