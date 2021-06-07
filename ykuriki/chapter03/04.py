import numpy as np


# パラメータ
fs = 44100
n1 = 1
r1 = 1.5
theta1 = 0.3
n2 = 3
r2 = 0.3
theta2 = 1.1

t = np.arange(0, fs) / fs
x = r1 * np.cos(2 * np.pi * n1 * t - theta1) + r2 * np.cos(2 * np.pi * n2 * t - theta2)

a = 2 / fs * sum(x * np.cos(2 * np.pi * t))
b = 2 / fs * sum(x * np.sin(2 * np.pi * t))

print("1[Hz]")
print(f"amplitude: {np.sqrt(a**2+b**2):.10f}")
print(f"phase    : {np.arctan2(b,a):.10f}")


# 3Hzに変えて実行
a = 2 / fs * sum(x * np.cos(2 * np.pi * t * 3))
b = 2 / fs * sum(x * np.sin(2 * np.pi * t * 3))

print("3[Hz]")
print(f"amplitude: {np.sqrt(a**2+b**2):.10f}")
print(f"phase    : {np.arctan2(b,a):.10f}")
