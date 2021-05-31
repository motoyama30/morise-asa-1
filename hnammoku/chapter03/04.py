# 正弦波の重ね合わせ
import numpy as np

# 信号の生成
fs = 44100
n1 = 1
r1 = 1.5
theta1 = 0.3
n2 = 3
r2 = 0.3
theta2 = 1.1
t = np.arange(fs) / fs
x = r1 * np.cos(2 * np.pi * n1 * t - theta1) + r2 * np.cos(2 * np.pi * n2 * t - theta2)

# a,bの推定
a = 2 / fs * np.sum(x * np.cos(2 * np.pi * t))
b = 2 / fs * np.sum(x * np.sin(2 * np.pi * t))

# 振幅と位相の計算（r1, theta1 と等しい）
print(f"振幅: {np.sqrt(a ** 2 + b ** 2)}")
print(f"位相: {np.arctan2(b, a)}")
