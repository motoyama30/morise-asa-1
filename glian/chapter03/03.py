import numpy as np

fs = 44100
r = 1.5
theta = 0.3
n = 2

# m!=2の時
m = 3
print("(m = {})".format(m))
t = np.arange(fs) / fs
x = r * np.cos(2 * np.pi * n * t - theta)
a = 2 / fs * np.sum(x * np.cos(2 * np.pi * m * t))
b = 2 / fs * np.sum(x * np.sin(2 * np.pi * m * t))

print("a: {}".format(a))
print("b: {}".format(b))
