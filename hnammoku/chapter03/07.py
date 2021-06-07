# FFTによるスペクトル解析
import numpy as np
import matplotlib.pyplot as plt

# 信号の生成
N = 8
x = np.random.randn(N)

# DFT
c = np.zeros(N).astype("complex")
for i in range(N):
    c[i] = np.sum(x * np.exp(-1j * 2 * np.pi * i * np.arange(N) / N))

# FFT
X = np.fft.fft(x, axis=0)

# 比較
print(np.isclose(c, X))
plt.plot(np.abs(c), label="c")
plt.plot(np.abs(X), label="X")
plt.plot(np.abs(c - X), label="c - X")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.show()
