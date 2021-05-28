import numpy as np

fs = 44100
f1 = 1
r1 = 1.5
theta1 = 0.3
f2 = 3
r2 = 0.2
theta2 = -1.1
t = np.arange(fs).reshape(1, fs)/fs
x = r1*np.cos(2*np.pi*f1*t - theta1) + r2*np.cos(2*np.pi*f2*t - theta2)
# 1 [Hz] の正弦波との内積
k1 = 1
c1 = np.sum(x*np.exp(-1j*2*np.pi*k1*t))/fs
k3 = 3
c3 = np.sum(x*np.exp(-1j*2*np.pi*k3*t))/fs

print("(f={})".format(k1))
print("r1/2: {}".format(np.abs(c1)))
print("theta1: {}".format(np.angle(np.conjugate(c1))))

print("(f={})".format(k3))
print("r3/2: {}".format(np.abs(c3)))
print("theta3: {}".format(np.angle(np.conjugate(c3))))