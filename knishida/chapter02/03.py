import numpy as np

N=1000
x1=np.random.randn(N)
x2=np.random.randn(N)
x1=x1-np.mean(x1)
x2=x2-np.mean(x2)

x1=x1**2
x2=x2**2

L_p=10*np.log10(np.sum(x1)/np.sum(x2))

print("L_p: "+str(L_p))