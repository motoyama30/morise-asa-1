# メインローブとサイドローブ
import numpy as np
import matplotlib.pyplot as plt

# 信号生成
fs = 44100
N = int(np.round(fs * 0.02))
fft_size = 65536
win_rect = np.ones(N)
W_rec = np.fft.fftshift(np.abs(np.fft.fft(win_rect, fft_size)))
W_rec = W_rec / np.max(W_rec)

# グラフ描画
w = np.arange(fft_size) * fs / fft_size - fs / 2
plt.plot(w, W_rec)
plt.xlim(-400, 400)
plt.ylim(0, 1)
plt.title("Amplitude spectrum of a rectangular window")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.show()
