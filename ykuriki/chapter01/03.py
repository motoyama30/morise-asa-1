import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


fs = 44100
t = np.arange(0, fs) / fs
# f = 1
f = 1000
x = np.sin(2 * np.pi * f * t)

plt.plot(t, x)
plt.show()

sd.play(x, fs)
status = sd.wait()
