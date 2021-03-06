# 移動平均フィルタ
import matplotlib.pyplot as plt
import numpy as np

# 信号とノイズ生成
fs = 1000
t = np.arange(fs) / fs
f = 1
signal = np.sin(2 * np.pi * f * t)
noise = np.random.randn(fs)
snr = 6
noise = np.sqrt(np.sum(signal ** 2) / np.sum(noise ** 2))

# 信号とノイズの混合
x = signal + noise

# フィルタリング
y = np.zeros(len(x))
m = 5
for i in range(len(y)):
    y[i] = np.mean(x[i - m : i + m])

# グラフ表示
plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.title("signal")
plt.subplot(3, 1, 2)
plt.plot(t, x)
plt.title("x")
plt.subplot(3, 1, 3)
plt.plot(t, y)
plt.title("y")
plt.show()
