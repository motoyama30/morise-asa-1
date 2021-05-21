import numpy as np
import matplotlib.pyplot as plt

n = np.arange(20)
omega = 0.1*2*np.pi

x1 = np.sin(omega*n)
x2 = np.sin((omega+2*np.pi)*n)

plt.subplot(2,1,1)
plt.plot(n,x1)
plt.title("sin(ωn)")
plt.grid()
plt.ylim(-1,1)

plt.subplot(2,1,2)
plt.plot(n,x2)
plt.title("sin((ω+2π)n)")
plt.grid()
plt.ylim(-1,1)

plt.show()

plt.figure()
plt.plot(n,x1-x2)
plt.ylim(-1,1)

plt.show()