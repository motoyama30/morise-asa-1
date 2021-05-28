import numpy as np

fs = 44100
f1 = 1
r1 = 1.5
theta1 = 0.3
f2 = 3
r2 = 0.2
theta2 = -1.1
t = np.arange(fs)/fs
k1 = 1
k3 = 3

x = r1*np.cos(2*np.pi*f1*t-theta1) + r2*np.cos(2*np.pi*f2*t-theta2)

c1 = np.sum(x*np.exp(-1j*2*np.pi*k1*t))/fs
c3 = np.sum(x*np.exp(-1j*2*np.pi*k3*t))/fs

print(abs(c1))
print(np.angle(np.conj(c1)))
