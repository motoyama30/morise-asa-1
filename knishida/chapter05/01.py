import numpy as np
import matplotlib.pyplot as plt


# declare
fs = 8000
t = np.arange(0, 1, 1 / fs)
f1 = 3.0
f2 = 3.5

# calc
x1 = np.array(np.cos(2 * np.pi * f1 * t))
X1 = np.abs(np.fft.fft(x1)) / len(x1)
x2 = np.array(np.cos(2 * np.pi * f2 * t))
X2 = np.abs(np.fft.fft(x2)) / len(x2)

# output
w = np.arange(0, len(t)) * fs / len(t)
ax1 = plt.subplot(2, 1, 1)
ax1.stem(w, X1)
ax1.set_xlim(0, 10)
ax1.set_xlabel("frequency [Hz]")
ax1.set_ylabel("Amplitude")
ax1.set_title("3Hz spectrum")
ax2 = plt.subplot(2, 1, 2)
ax2.stem(w, X2)
ax2.set_xlim(0, 10)
ax2.set_xlabel("frequency [Hz]")
ax2.set_ylabel("Amplitude")
ax2.set_title("3.5Hz spectrum")

plt.tight_layout()
plt.show()
