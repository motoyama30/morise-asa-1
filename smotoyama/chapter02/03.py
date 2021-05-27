import numpy as np


np.random.seed(30)
N = 1000

x1 = np.random.randn(N,1)
x2 = np.random.randn(N,1)

x1 = x1 - np.mean(x1)
x2 = x2 - np.mean(x2)

L_p = 10*np.log10(np.sum(x1**2)/np.sum(x2**2))

print(L_p)