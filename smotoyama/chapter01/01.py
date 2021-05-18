import numpy as np
import matplotlib.pyplot as plt

x=[1,3,-5,2]

fs=10
t=np.arange(len(x))/fs

plt.plot(t,x)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()
