import numpy as np

fs = 8
f = 0
r = 0.5
t = np.arange(fs)/fs
x = r*np.cos(2*np.pi*f*t)

c = np.sum(x*np.exp(-1j*2*np.pi*f*t))/fs

print(abs(c))
