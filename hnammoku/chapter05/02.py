# FFT長の延長
import numpy as np
import matplotlib.pyplot as plt

# 信号生成
fs = 8000
t = np.arange(fs) / fs
f1 = 3
f2 = 3.5
x1 = np.cos(2 * np.pi * f1 * t)
x2 = np.cos(2 * np.pi * f2 * t)
fft_size = 2 ** 17
X1 = np.abs(np.fft.fft(x1, fft_size)) / np.size(x1)
X2 = np.abs(np.fft.fft(x2, fft_size)) / np.size(x2)
X1_stem = np.abs(np.fft.fft(x1)) / np.size(x1)
X2_stem = np.abs(np.fft.fft(x2)) / np.size(x2)
# グラフ描画
w = np.arange(fft_size) * fs / fft_size
w_stem = np.arange(np.size(t)) * fs / np.size(t)
plt.subplot(2, 1, 1)
plt.stem(w_stem, X1_stem, use_line_collection=True)
plt.plot(w, X1, "--")
plt.xlim(0, 10)
plt.title("3Hz spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.subplot(2, 1, 2)
plt.stem(w_stem, X2_stem, use_line_collection=True)
plt.plot(w, X2, "--")
plt.xlim(0, 10)
plt.title("3.5Hz spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()
