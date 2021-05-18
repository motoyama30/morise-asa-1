import numpy as np
import matplotlib.pyplot as plt

X=[1,3,-5,2]
fs=10
t=np.arange(len(X))/fs

plt.plot(t,X)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()
