import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 44100
N = round(fs * 0.02)
fft_size = 65536

win_rect = np.ones(N)
W_rec = np.fft.fftshift(abs(np.fft.fft(win_rect, fft_size)))
W_rec = W_rec / max(W_rec)

w = np.arange(0, fft_size) / fft_size * fs - fs / 2

# プロット
plt.plot(w, W_rec)
plt.xlim(-400, 400)
plt.xlabel("frequency [Hz]")
plt.ylim(0, 1)
plt.ylabel("amplitude")
plt.grid()
plt.show()
