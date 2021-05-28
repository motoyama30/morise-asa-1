import numpy as np


<<<<<<< HEAD
# パラメータ
fs = 8
# fs = 7
# 0から8まで変えてみる
f = [0, 1, 2, 3, 4, 5, 6, 7, 8]
r = 0.5

t = np.arange(0, fs) / fs

for i in f:
    x = r * np.cos(2 * np.pi * i * t)
    c = sum(x * np.exp(-1j * 2 * np.pi * i * t) / fs)
    print(f"amplitude(f={i}): {abs(c):.10f}")
=======
##パラメータ
fs = 8
#fs = 7
##0から8まで変えてみる
f = [0,1,2,3,4,5,6,7,8]
r = 0.5

t = np.arange(0,fs)/fs

for i in f:
    x = r*np.cos(2*np.pi*i*t)
    c = sum(x*np.exp(-1j*2*np.pi*i*t)/fs)
    print(f'amplitude(f={i}): {abs(c):.10f}')
>>>>>>> ade158846085480320c13d37c2b26953dd679278
