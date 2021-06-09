# 単位インパルス関数を対象にした位相スペクトルの解析
import numpy as np
import matplotlib.pyplot as plt

# 信号の生成
fs = 8000
x = np.zeros(fs)
m = 1
x[m] = 1
fft_size = 2 ** np.ceil(np.log2(len(x)))
X = np.fft.fft(x, int(fft_size), axis=0)

# 位相スペクトル表示
plt.subplot(2, 1, 1)
w = np.arange(fft_size).T * fs / fft_size
plt.plot(w, np.angle(X))
plt.title("Phase spectrum")
plt.xlabel("Frequency[Hz]")
plt.ylabel("Phase[rad]")

# 位相のアンラップ処理
plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(X)))
plt.title("Phase spectrum of the unwrapped signal")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Phase [rad]")
plt.show()
