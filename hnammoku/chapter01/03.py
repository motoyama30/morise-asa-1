# 正弦波
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
fs = 41000
np.arange(fs)
t = np.arange(fs)/fs
f = 1
x = np.sin(2*np.pi*f*t)
plt.plot(t,x)
sd.play(x,fs)
status = sd.wait()