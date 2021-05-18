import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,3,-5,2])

plt.plot(x)
plt.xlabel("Array Number")
plt.ylabel("Amplitude")
plt.show()

# 標本化周期を10Hzにして、横軸を秒にする
fs = 10
t = np.arange(len(x))/fs
print(t)
plt.plot(t,x)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()