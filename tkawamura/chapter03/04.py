import numpy as np

fs = 44100
n1 = 1
r1 = 1.5
theta1 = 0.3
n2 = 3
r2 = 0.3
theta2 = 1.1
t = np.arange(fs).reshape(1, fs)/fs
x = r1*np.cos(2*np.pi*n1*t - theta1) + r2*np.cos(2*np.pi*n2*t - theta2)
# 1 [Hz] の正弦波との内積
f = 1
print("(f={})".format(f))
a = 2/fs*np.sum(x*np.cos(2*np.pi*f*t))
b = 2/fs*np.sum(x*np.sin(2*np.pi*f*t))

print("r: {}".format(np.sqrt(a**2 + b**2)))
print("theta: {}".format(np.arctan2(b, a)))

# 3 [Hz] の正弦波との内積
f = 3
print("(f={})".format(f))
a = 2/fs*np.sum(x*np.cos(2*np.pi*f*t))
b = 2/fs*np.sum(x*np.sin(2*np.pi*f*t))

print("r: {}".format(np.sqrt(a**2 + b**2)))
print("theta: {}".format(np.arctan2(b, a)))