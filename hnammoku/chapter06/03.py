# IIRフィルタのスペクトル解析
import numpy as np
import matplotlib.pyplot as plt

# 差分方程式による振幅スペクトル計算
N = 128
k = np.arange(0, N)
spec1 = abs(1 / (1 - 0.5 * np.exp(-1j * 2 * np.pi * k / N)))

# インパルス応答による振幅スペクトル計算
h = np.zeros(N)
h[0] = 1
for n in range(1, N):
    h[n] = 0.5 * h[n - 1]
spec2 = abs(np.fft.fft(h))

# グラフ描画
fig = plt.figure()

plt.subplot(2, 1, 1)
plt.plot(k, spec1)
plt.xlim(0, N - 1)
plt.xlabel("Discrete frequency")
plt.ylabel("Amplitude")
plt.title("spec1")

plt.subplot(2, 1, 2)
plt.plot(k, spec2)
plt.xlim(0, N - 1)
plt.xlabel("Discrete frequency")
plt.ylabel("Amplitude")
plt.title("spec2")

plt.tight_layout()
plt.show()
