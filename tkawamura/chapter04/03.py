import matplotlib.pyplot as plt
import numpy as np

fs = 44100
t = np.arange(fs).reshape(fs, 1) / fs  # 信号長が1秒分
f = 5
x = np.sin(2 * np.pi * f * t)
fft_size = int(2 ** np.ceil(np.log2(len(x))))  # int型へキャスティング
X1 = np.fft.fft(x, axis=0)
X2 = np.fft.fft(x, fft_size, axis=0)

print(f"{np.sum(x**2):.2f}")
print(f"{np.sum(np.abs(X1)**2)/len(X1):.2f}")
print(f"{np.sum(np.abs(X2)**2)/fft_size:.2f}")
