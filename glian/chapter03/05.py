import numpy as np

fs = 44100
f1 = 1
r1 = 1.5
theta1 = 0.3
f2 = 3
r2 = 0.2
theta2 = -1.1
t = np.arange(fs) / fs
x = r1 * np.cos(2 * np.pi * f1 * t - theta1) + r2 * np.cos(2 * np.pi * f2 * t - theta2)
f1 = 1
c1 = np.sum(x * np.exp(-1j * 2 * np.pi * f1 * t)) / fs
f2 = 3
c2 = np.sum(x * np.exp(-1j * 2 * np.pi * f2 * t)) / fs

print("(f={})".format(k1))
print("r1/2: {}".format(np.abs(c1)))
print("theta1: {}".format(np.angle(np.conjugate(c1))))

print("(f={})".format(k2))
print("r2/2: {}".format(np.abs(c2)))
print("theta2: {}".format(np.angle(np.conjugate(c2))))
