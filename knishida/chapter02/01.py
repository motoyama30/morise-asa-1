import numpy as np
import matplotlib.pyplot as plt

fs=44100
t=np.arange(0, 0.5, 1/fs)

x=np.array(np.sin(2*np.pi*t))

S=np.sum(x)/fs

print("S="+str(S))

plt.plot(t,x)
plt.show()
