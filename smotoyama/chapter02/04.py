import numpy as np
import matplotlib.pyplot as plt

fs = 44100
t = np.arange(fs).reshape(fs,1)/fs

x1 = np.zeros((fs,1))
x1[int(fs/2)-500+1:int(fs/2)+500+1] = 1
x2 = np.zeros((fs,1))
x2[int(fs/4)-1000+1:int(fs/4)+1000+1] = 1


plt.subplot(2,1,1)
plt.plot(t,x1)
plt.title("x1")
plt.grid()
plt.ylim(0,1)

plt.subplot(2,1,2)
plt.plot(t,x2)
plt.title("x2")
plt.grid()
plt.ylim(0,1)

plt.show()

energy = np.sum(x1**2)/fs
xx1 = x1/np.sqrt(energy)
t_c = np.sum(t*xx1**2)/fs

print('{:.10g}'.format(t_c))

sigma_t = np.sum((t-t_c)**2*xx1**2)/fs

print('{:.10g}'.format(sigma_t))

t_c1 = np.sum(t*xx1**2)/fs
t_c2 = np.sum(t**2*xx1**2)/fs
sigma_t = t_c2 - t_c1**2

print('{:.10g}'.format(sigma_t))

print('{:.10g}'.format(fs/np.sum(x1**2)/3*(2*(500.5/fs)**3)))
