import numpy as np


N = 1000
#np.random.seed(0)
x1 = np.random.randn(N)
x2 = np.random.randn(N)

x1 = x1-np.mean(x1)
x2 = x2-np.mean(x2)

L_p = 10*np.log10(sum(x1**2)/sum(x2**2))
print(L_p)