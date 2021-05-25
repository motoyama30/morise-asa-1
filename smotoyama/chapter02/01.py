import numpy as np

fs = 44100
t = np.arange(fs/2)
t = t/fs
x = np.sin(2*np.pi*t)

S = np.sum(x)/fs

print(S)