import matplotlib.pyplot as plt
import numpy as np

fs = 8000
x = np.zeros((fs, 1))
m = 1
x[m] = 1
fft_size = int(2 ** np.ceil(np.log2(len(x))))
X = np.fft.fft(x, fft_size, axis=0)

plt.subplot(2, 1, 1)
w = np.arange(fft_size) * fs / fft_size
plt.plot(w, np.angle(X))
plt.xlabel("Frequency [Hz]")
plt.grid()

# 位相のアンラップ
plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(X[:, 0])))
plt.xlabel("Frequency [Hz]")
plt.grid()
plt.tight_layout()
plt.show()
