import numpy as np
import matplotlib.pyplot as plt


# declare
fs = 44100
fft_size = 65536
w = np.arange(0, 1, 1 / fft_size) * fs

# calc and output
plt.plot(w / 1000, np.abs(np.fft.fft(np.array([0.5, -0.5]), fft_size)))
plt.xlim(0, fs / 2000)
plt.xlabel("frequency (Hz)")
plt.ylabel("amplitude")
plt.show()
