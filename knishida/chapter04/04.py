import numpy as np


# declare
fs = 44100
t = np.arange(0, 1, 1 / fs)
f1 = 10
f2 = 100
r1 = 1
r2 = 2
x1 = np.array(r1 * np.sin(2 * np.pi * f1 * t))
x2 = np.array(r2 * np.sin(2 * np.pi * f2 * t))

# calc
x = x1 + x2
X = np.fft.fft(x)

p1 = 20 * np.log10(np.sum(np.abs(X[0:20])))
p2 = 20 * np.log10(np.sum(np.abs(X[90:110])))

# output
print("{:.2f}".format(np.sum(x1 ** 2)))
print("{:.2f}".format(np.sum(x2 ** 2)))
print("{:.2f}".format(np.sum(x ** 2)))
print(p1)
print(p2)
