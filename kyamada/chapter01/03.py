import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

fs = 44100
len_t = 1
t = np.arange(fs * len_t) / fs
print(t)
f = 1

x = np.sin(2 * np.pi * f * t)
plt.plot(x)
plt.show()

sd.play(x, fs)
status = sd.wait()
