import numpy as np
import matplotlib.pyplot as plt

fs = 44100
N = np.round(fs * 0.02)
fft_size = 65536
win_rect = np.ones(int(N))
w = np.arange(fft_size) / fft_size * fs - fs / 2

# cal
W_rec = np.fft.fftshift(abs(np.fft.fft(win_rect, fft_size)))
W_rec = W_rec / np.max(W_rec)

# plot
plt.plot(w, W_rec)
plt.xlabel("周波数[Hz]")
plt.ylabel("振幅")
plt.xlim(-400.400)
plt.ylim(0, 1)
plt.grid()
plt.show()
