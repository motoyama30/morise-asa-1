import numpy as np
import matplotlib.pyplot as plt


# declare
fs = 44100
N = np.round(fs * 0.02)
fft_size = 65536
win_rect = np.ones(int(N))

# calc
W_rec = np.fft.fftshift(np.abs(np.fft.fft(win_rect, fft_size)))
W_rec = W_rec / np.max(W_rec)

# output
w = np.arange(0, fft_size) / fft_size * fs - fs / 2
plt.plot(w, W_rec)
plt.xlim(-400, 400)
plt.ylim(0, 1)
plt.xlabel("frequency [Hz]")
plt.ylabel("Amplitude")
plt.show()
