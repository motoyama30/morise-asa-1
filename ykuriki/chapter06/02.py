import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 44100
fft_size = 65536

w = np.arange(0, fft_size) / fft_size * fs

# プロット
plt.plot(w / 1000, abs(np.fft.fft(np.array([0.5, -0.5]), fft_size)))
plt.xlim(0, fs / 2000)
plt.xlabel("frequency [kHz]")
plt.ylabel("amplitude")
plt.grid()

plt.show()
