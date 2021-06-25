import numpy as np


# パラメータ
fs = 44100
f1 = 10
f2 = 100
r1 = 1
r2 = 2

t = np.arange(0, fs) / fs
x1 = r1 * np.sin(2 * np.pi * f1 * t)
x2 = r2 * np.sin(2 * np.pi * f2 * t)
x = x1 + x2
X = np.fft.fft(x)

print(f"x1: {sum(x1**2):.2f}")
print(f"x2: {sum(x2**2):.2f}")
print(f"x : {sum(x**2):.2f}")

p1 = 20 * np.log10(sum(abs(X[0:20])))
p2 = 20 * np.log10(sum(abs(X[90:110])))

print(f"p1: {p1:.10f}")
print(f"p2: {p2:.10f}")
