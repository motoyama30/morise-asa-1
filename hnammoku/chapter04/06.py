# 位相遅延の確認
import numpy as np
import matplotlib.pyplot as plt

fs = 44100
fft_size = 65536
x = np.zeros(fft_size)
x[1] = 1
X = np.fft.fft(x, fft_size, axis=0)

# 波形表示
w = np.arange(fft_size).T / fft_size * fs
phase_delay = -np.unwrap(np.angle(X)) / (2 * np.pi * w)
plt.plot(w, phase_delay * fs)
plt.title("Phase Delay")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Sample")
plt.show()
