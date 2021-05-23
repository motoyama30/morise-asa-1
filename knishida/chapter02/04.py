import numpy as np
import matplotlib.pyplot as plt

fs=44100
t=np.arange(0,1,1/fs)

x1=np.zeros(fs)
x1[fs//2-500:fs//2+500]=1

x2=np.zeros(fs)
x2[fs//4-1000:fs//4+1000]=1

energy=sum(x1**2)/fs
xx1=x1/np.sqrt(energy)
t_c=np.sum(t*(xx1**2))/fs

sigma_t2=np.sum(((t-t_c)**2)*(xx1**2))/fs

t_c2=np.sum((t**2)*(xx1**2))/fs
sigma_t3=t_c2-t_c**2

sigma_t4=fs/np.sum(x1**2)/3*(2*(500.5/fs)**3)

print("No.1:"+str(t_c))
print("No.2:"+str(sigma_t2))
print("No.3:"+str(sigma_t3))
print("No.4:"+str(sigma_t4))