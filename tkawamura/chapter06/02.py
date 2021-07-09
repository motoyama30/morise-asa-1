import matplotlib.pyplot as plt
import numpy as np

fs = 44100
fft_size = 65536

w = np.arange(fft_size) / fft_size * fs

plt.plot(w / 1000, np.abs(np.fft.fft(np.array([0.5, -0.5]), fft_size)))

plt.xlim(0, fs / 2000)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")

plt.grid()
plt.show()
