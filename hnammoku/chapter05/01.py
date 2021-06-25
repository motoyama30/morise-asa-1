# 信号のスペクトル算出
import numpy as np
import matplotlib.pyplot as plt

# 信号生成
fs = 8000
t = np.arange(fs) / fs
f1 = 3
f2 = 3.5
x1 = np.cos(2 * np.pi * f1 * t)
X1 = np.abs(np.fft.fft(x1)) / np.size(x1)
x2 = np.cos(2 * np.pi * f2 * t)
X2 = np.abs(np.fft.fft(x2)) / np.size(x2)

# グラフ描画
w = np.arange(np.size(t)) * fs / np.size(t)
plt.subplot(2, 1, 1)
plt.stem(w, X1, use_line_collection=True)
plt.xlim(0, 10)
plt.title("3 Hz spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.subplot(2, 1, 2)
plt.stem(w, X2, use_line_collection=True)
plt.xlim(0, 10)
plt.title("3.5Hz spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()
