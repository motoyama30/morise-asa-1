# 正弦波の周波数推定
import numpy as np

# 信号の生成
fs = 44100
r = 1.5
theta = 0.3
n = 2
m = 3
t = np.arange(fs) / fs
x = r * np.cos(2 * np.pi * n * t - theta)

# a,bの推定（n≠mのとき0に近い値になる）
a = 2 / fs * np.sum(x * np.cos(2 * np.pi * m * t))
b = 2 / fs * np.sum(x * np.sin(2 * np.pi * m * t))
print(f"n = {n}, m = {m} のとき")
print(f"a = {a}")
print(f"b = {b}")
