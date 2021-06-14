# パーセバルの定理による漏れ誤差の解釈
import numpy as np

# 信号生成
fs = 44100
t = np.arange(fs) / fs
f1 = 10
f2 = 100
r1 = 1
r2 = 2
x1 = r1 * np.sin(2 * np.pi * f1 * t)
x2 = r2 * np.sin(2 * np.pi * f2 * t)
x = x1 + x2
X = np.fft.fft(x, axis=0)

# パワー総和確認
print(f"x1のパワー総和：{np.sum(x1**2):.2f}")
print(f"x2のパワー総和：{np.sum(x2**2):.2f}")
print(f"xのパワー総和：{np.sum(x**2):.2f}")

# デシベル単位でのパワー算出
p1 = 20 * np.log10(np.sum(np.abs(X[1:19])))
p2 = 20 * np.log10(np.sum(np.abs(X[90:109])))
print(f"10Hz周辺のパワー：{p1:.2f}")
print(f"100Hz周辺のパワー：{p2:.2f}")
