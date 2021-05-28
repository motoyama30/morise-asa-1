import numpy as np


# パラメータ
fs = 44100
r = 1.5
theta = 0.3
f = 2
L = 1 / f

t = np.arange(0, fs * L) / fs
x = r * np.cos(2 * np.pi * t / L - theta)

a = 2 / fs / L * sum(x * np.cos(2 * np.pi * t / L))
b = 2 / fs / L * sum(x * np.sin(2 * np.pi * t / L))

print(f"amplitude: {np.sqrt(a**2+b**2):.10f}")
print(f"phase    : {np.arctan2(b,a):.10f}")
