# パーセバルの定理による漏れ誤差の解釈
import numpy as np

# 信号生成
fs = 44100
t = np.arange(fs) / fs
f = 5
x = np.sin(2 * np.pi * f * t)
fft_size = 2 ** np.ceil(np.log2(len(x)))
X1 = np.fft.fft(x, axis=0)
X2 = np.fft.fft(x, int(fft_size), axis=0)

# パワー総和確認
print(f"xのパワー総和：{np.sum(x**2):.2f}")
print(f"X1のパワー総和：{np.sum(np.abs(X1)**2)/len(X1):.2f}")
print(f"X2のパワー総和：{np.sum(np.abs(X2)**2)/fft_size:.2f}")
