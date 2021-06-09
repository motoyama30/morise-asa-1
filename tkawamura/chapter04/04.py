import matplotlib.pyplot as plt
import numpy as np

fs = 44100
t = np.arange(fs).reshape(fs, 1) / fs
f1 = 10
f2 = 100
r1 = 1
r2 = 2
x1 = r1 * np.sin(2 * np.pi * f1 * t)
x2 = r2 * np.sin(2 * np.pi * f2 * t)
x = x1 + x2
X = np.fft.fft(x, axis=0)

# 時間領域でのパワーが等しくなることの確認
print(f"{np.sum(x1**2):.2f}")
print(f"{np.sum(x2**2):.2f}")
print(f"{np.sum(x**2):.2f}")

p1 = 20 * np.log10(np.sum(np.abs(X[1:20])))
p2 = 20 * np.log10(np.sum(np.abs(X[91:110])))

# 6 [dB] ほどの差を確認できる．
print(f"{p1:.2f}")
print(f"{p2:.2f}")
