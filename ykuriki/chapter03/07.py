import numpy as np


<<<<<<< HEAD
# パラメータ
=======
##パラメータ
>>>>>>> ade158846085480320c13d37c2b26953dd679278
N = 8

x = np.random.randn(N)

c = np.zeros(N, dtype=complex)
<<<<<<< HEAD
for i in range(0, N):
    c[i] = sum(x * np.exp(-1j * 2 * np.pi * i * np.arange(0, N) / N))

X = np.fft.fft(x)

# print(f'c = {c}')
# print(f'X = {X}')
print(np.isclose(c, X))
=======
for i in range(0,N):
    c[i] = sum(x*np.exp(-1j*2*np.pi*i*np.arange(0,N)/N))

X = np.fft.fft(x)

#print(f'c = {c}')
#print(f'X = {X}')
print(np.isclose(c,X))
>>>>>>> ade158846085480320c13d37c2b26953dd679278
