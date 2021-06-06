import numpy as np

fs = 44100
t = np.arange(fs) / fs
f1 = 10
f2 = 100
r1 = 1
r2 = 2
x1 = r1 * np.sin(2 * np.pi * f1 * t)
x2 = r2 * np.sin(2 * np.pi * f2 * t)

x = x1 + x2
X = np.fft.fft(x)
p1 = 20 * np.log10(np.sum(abs(X[0:19])))
p2 = 20 * np.log10(np.sum(abs(X[90:109])))

print("{:.2f}".format(np.sum(x1 ** 2)))
print("{:.2f}".format(np.sum(x2 ** 2)))
print("{:.2f}".format(np.sum(x ** 2)))
print(p1)
print(p2)
