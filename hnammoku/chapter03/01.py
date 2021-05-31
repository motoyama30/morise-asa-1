# パラメータ推定の検証
import numpy as np

# 信号の生成
fs = 44100
t = np.arange(fs) / fs
r = 1.5
theta = 0.3
x = r * np.cos(2 * np.pi * t - theta)

# a,bの推定
a = 2 / fs * np.sum(x * np.cos(2 * np.pi * t))
b = 2 / fs * np.sum(x * np.sin(2 * np.pi * t))

# 振幅と位相の計算
print(f"振幅: {np.sqrt(a ** 2 + b ** 2)}")
print(f"位相: {np.arctan2(b, a)}")
