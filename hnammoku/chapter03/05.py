# 複素数による係数の統合
import numpy as np

# 解析信号の生成
fs = 44100
n1 = 1
r1 = 1.5
theta1 = 0.3
n2 = 3
r2 = 0.3
theta2 = 1.1
t = np.arange(fs) / fs
x = r1 * np.cos(2 * np.pi * n1 * t - theta1) + r2 * np.cos(2 * np.pi * n2 * t - theta2)

# c_kの計算
k1 = 1
c1 = np.sum(x * np.exp(-1j * 2 * np.pi * k1 * t)) / fs
k3 = 3
c3 = np.sum(x * np.exp(-1j * 2 * np.pi * k3 * t)) / fs

# 振幅と位相の計算
print(f"{k1}[Hz]のとき")
print(f"振幅: {np.abs(c1)}")
print(f"位相: {np.angle(np.conj(c1))}")
print(f"{k3}[Hz]のとき")
print(f"振幅: {np.abs(c3)}")
print(f"位相: {np.angle(np.conj(c3))}")
