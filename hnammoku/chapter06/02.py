# フィルタのスペクトル解析
import numpy as np
import matplotlib.pyplot as plt

# 信号生成
fs = 44100
fft_size = 65536
w = np.arange(0, fft_size) / fft_size * fs

# グラフ描画
plt.plot(w / 1000, abs(np.fft.fft(np.array([0.5, -0.5]), fft_size)))
plt.xlim(0, fs / 2000)
plt.xlabel("Frequency [kHz]")
plt.ylabel("Amplitude")

plt.show()
