import numpy as np


##パラメータ
fs = 44100
r = 1.5
theta = 0.3

t = np.arange(0,fs)/fs
x = r*np.cos(2*np.pi*t-theta)

a = 2/fs*sum(x*np.cos(2*np.pi*t))
b = 2/fs*sum(x*np.sin(2*np.pi*t))

print(f'amplitude: {np.sqrt(a**2+b**2):.10f}')
print(f'phase    : {np.arctan2(b,a):.10f}')