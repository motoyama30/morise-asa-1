import numpy as np
import matplotlib.pyplot as plt

fs = 44100
fft_size = 65536
w = np.arange(fft_size) * fs / fft_size

plt.plot(w / 1000, abs(np.fft.fft(np.array([0.5, -0.5]), fft_size)))
plt.xlabel("frequency (Hz)")
plt.ylabel("amplitude")
plt.xlim(0, fs / 2000)
plt.show()
