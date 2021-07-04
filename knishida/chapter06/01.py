import numpy as np
import simpleaudio as sa


# declare
fs = 44100
x = np.random.randn(fs)
y = np.zeros(fs)
y[0] = 0.5 * x[0]
for n in range(1, len(x)):
    y[n] = 0.5 * x[n] - 0.5 * x[n - 1]


play_obj = sa.play_buffer(x, 2, 2, 44100)
play_obj.wait_done()
play_obj = sa.play_buffer(y, 2, 2, 44100)
play_obj.wait_done()
