import numpy as np
import matplotlib.pyplot as plt


# declare
fs = 8000
x = np.zeros(fs)
m = 1
x[m] = 1
fft_size = 2 ** np.ceil(np.log2(len(x)))

# calc
X = np.fft.fft(x, int(fft_size))

# output
w = np.arange(0, fft_size) * fs / fft_size
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)
ax1.plot(w, np.angle(X))
ax2.plot(w, np.unwrap(np.angle(X)))
ax1.set_xlabel("frequency [Hz]")
ax2.set_xlabel("frequency [Hz]")
ax1.set_ylabel("angle [rad]")
ax2.set_ylabel("angle [rad]")
ax1.set_title("angle from frequency")
ax2.set_title("unwraped angle from frequency")

plt.tight_layout()
plt.show()
