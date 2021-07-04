import numpy as np
import sounddevice as sd

fs = 44100
x = np.random.randn(fs)
y = np.zeros(fs)

y[0] = 0.5 * x[0]
for n in range(1, len(x)):
    y[n] = 0.5 * x[n] - 0.5 * x[n - 1]

sd.play(x, fs)
sd.wait()

sd.play(y, fs)
sd.wait()
