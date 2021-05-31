import numpy as np

fs = 44100
r = 1.5
theta = 0.3
f = 2
L = 1 / f
t = np.arange(fs * L) / fs
x = r * np.cos(2 * np.pi * t / L - theta)

a = 2 / fs / L * np.sum(x * np.cos(2 * np.pi * t / L))
b = 2 / fs / L * np.sum(x * np.sin(2 * np.pi * t / L))

print(np.sqrt(a ** 2 + b ** 2))
print(np.arctan2(b, a))
