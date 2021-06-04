import numpy as np

N = 8
t = np.arange(0, N) / N
x = np.random.randn(8)
c = np.zeros(8)

for i in range(N):
    c[i] = np.sum(x * np.exp(-1j * 2 * np.pi * i * t))

X = np.fft.fft(x)

print(c)
print(X)
