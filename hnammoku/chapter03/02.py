# 周期の拡張
import numpy as np

# 信号の生成
fs = 44100
r = 1.5
theta = 0.3
f = 2
L = 1 / f
t = np.arange(fs * L) / fs
x = r * np.cos(2 * np.pi * t / L - theta)

# a,bの推定
a = 2 / fs / L * np.sum(x * np.cos(2 * np.pi * t / L))
b = 2 / fs / L * np.sum(x * np.sin(2 * np.pi * t / L))

# 振幅と位相の計算
print(f"振幅: {np.sqrt(a ** 2 + b ** 2)}")
print(f"位相: {np.arctan2(b, a)}")
