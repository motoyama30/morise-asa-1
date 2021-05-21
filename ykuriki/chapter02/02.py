import numpy as np
import matplotlib.pyplot as plt


n = np.arange(0,21)
omega = 0.1*2*np.pi
x1 = np.sin(omega*n)
x2 = np.sin((omega+2*np.pi)*n)

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.plot(n, x1)
ax2 = fig.add_subplot(2,1,2)
ax2.plot(n, x2)

plt.figure() 
plt.plot(x1-x2)

plt.figure()
plt.plot(x1-x2)
plt.ylim(-1, 1)
plt.show()