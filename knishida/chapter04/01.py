import numpy as np
import matplotlib.pyplot as plt


# declare
fs = 44100
t = np.arange(0, 2, 1 / fs)
f = 5
x = np.array(np.sin(2 * np.pi * f * t))

# calc
X = np.fft.fft(x)

# output
w = np.arange(0, len(x)) * fs / len(x)
plt.plot(w, np.abs(X))
plt.xlim(0, 50)
plt.ylabel("spectrum")
plt.xlabel("frequency [Hz]")
plt.show()
