import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

fs = 44100
len_t = 1 # (s)
t = np.arange(fs*len_t)/fs
print(t.shape)
f = 1
x = np.sin(2*np.pi*f*t)
plt.plot(t,x)
#plt.show()
plt.close()
sd.play(x,fs)
status = sd.wait()  # Wait until file is done playing
