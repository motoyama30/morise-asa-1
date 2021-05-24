# 平均時間・持続時間の計算
import numpy as np
import matplotlib.pyplot as plt

# 信号生成
fs = 41000
t = np.arange(fs) / fs
x = np.zeros(fs)
x[fs // 2 - 500 + 1 : fs // 2 + 500 + 1] = 1

energy = np.sum(x ** 2) / fs
xx = x / np.sqrt(energy)
meantime = np.sum(t * xx ** 2) / fs
sigma1 = np.sum((t - meantime) ** 2 * xx ** 2) / fs
sigma2 = np.sum(t ** 2 * xx ** 2) / fs - meantime ** 2
sigma3 = (fs / np.sum(x ** 2)) / 3 * (2 * (500.5 / fs) ** 3)

print(f"平均時間 : {meantime}")
print(f"持続時間（式15）: {sigma1}")
print(f"持続時間（式16）: {sigma2}")
print(f"持続時間（式17,18）: {sigma3}")

plt.plot(t, x)
plt.show()
