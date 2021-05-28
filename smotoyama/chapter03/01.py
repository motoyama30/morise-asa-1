import numpy as np

fs = 44100
t = np.arange(fs)/fs
r = 1.5
theta = 0.3
x = r*np.cos(2*np.pi*t-theta)

a = 2/fs*np.sum(x*np.cos(2*np.pi*t))
b = 2/fs*np.sum(x*np.sin(2*np.pi*t))

print(np.sqrt(a**2+b**2))
print(np.arctan2(b,a))
