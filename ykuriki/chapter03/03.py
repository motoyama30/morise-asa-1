import numpy as np


##パラメータ
fs = 44100
r = 1.5
theta = 0.3
#mの数値を変えてみる
n = 2
m = 3
#m = 2

t = np.arange(0,fs)/fs
x = r*np.cos(2*np.pi*n*t-theta)

a = 2/fs*sum(x*np.cos(2*np.pi*m*t))
b = 2/fs*sum(x*np.sin(2*np.pi*m*t))

print(f'a: {a:.16f}')
print(f'b: {b:.16f}')