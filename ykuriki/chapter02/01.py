import numpy as np


fs = 44100
t = np.arange(0, fs / 2) / fs
x = np.sin(2 * np.pi * t)

S = sum(x) / fs
print(S)
