import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 3, -5, 2])

plt.plot(x)
plt.show()


fs = 10
t = np.arange(x.size) / 10
plt.plot(t, x)

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.show()
