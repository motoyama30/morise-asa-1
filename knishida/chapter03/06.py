import numpy as np


fs=8
r=0.5
t=np.arange(0,1,1/fs)
for f in range(9):
    x=np.array(r*np.cos(2*np.pi*f*t))
    c=np.sum(x*np.exp(-1j*2*np.pi*f*t))/fs
    r_c=np.abs(c)
    print("f="+str(f)+":"+str(r_c))
