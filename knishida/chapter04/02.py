import numpy as np
import matplotlib.pyplot as plt


# declare
fs = 44100
t = np.arange(0, 1, 1 / fs)
f = 5
x = np.array(np.sin(2 * np.pi * f * t))
fft_size = 2 ** np.ceil(np.log2(len(x)))

# calc
X1 = np.fft.fft(x)
X2 = np.fft.fft(x, int(fft_size))

# output
w = np.arange(0, fft_size) * fs / fft_size
plt.plot(w, np.abs(X2))
plt.xlim(0, 50)
plt.xlabel("frequency [Hz}")
plt.ylabel("Amplitude")
plt.show()
