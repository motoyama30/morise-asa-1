# 区分求積法
import numpy as np

fs = 10
t = np.arange(fs / 2) / fs
f = 1
T = 0.5
x = np.sin(2 * np.pi * f * t)
S = sum(x) * T / fs
print(S)
