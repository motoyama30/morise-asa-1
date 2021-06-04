import numpy as np
import matplotlib.pyplot as plt

fs = 8000
x = np.zeros(fs)
m = 1
x[m] = 1
fft_size = 2 ** np.ceil(np.log2(len(x)))
w = np.arange(fft_size) / fft_size * fs

X = np.fft.fft(x, int(fft_size))

plt.subplot(2, 1, 1)
plt.plot(w, np.angle(X))
plt.xlabel("周波数[Hz]")
plt.ylabel("位相[rad]")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(X)))
plt.xlabel("周波数[Hz]")
plt.ylabel("位相[rad]")
plt.grid()

plt.tight_layout()
