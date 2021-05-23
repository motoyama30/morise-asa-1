import numpy as np
import matplotlib.pyplot as plt


n = np.arange(0,21)
omega = 0.1*2*np.pi
x1 = np.sin(omega*n)
x2 = np.sin((omega+2*np.pi)*n)


##結果のプロット
fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax1.plot(n, x1)
ax1.set_xlabel('Time [sample]')
ax1.set_ylabel('Amplitude')
ax1.set_title('sin(ω*n)')

ax2 = fig.add_subplot(2,1,2)
ax2.plot(n, x2)
ax2.set_xlabel('Time [sample]')
ax2.set_ylabel('Amplitude')
ax2.set_title('sin{(ω+2π)*n}')

plt.tight_layout()


plt.figure() 
plt.plot(x1-x2)
plt.xlabel('Time [sample]')
plt.ylabel('Amplitude')
plt.title('sin(ω*n)-sin{(ω+2π)*n}')

plt.figure()
plt.plot(x1-x2)
plt.xlabel('Time [sample]')
plt.ylim(-1, 1)
plt.ylabel('Amplitude')
plt.title('sin(ω*n)-sin{(ω+2π)*n}')

plt.show()