import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 8000
m = 1

x = np.zeros(fs)
x[m] = 1
fft_size = int(2 ** np.ceil(np.log2(len(x))))
X = np.fft.fft(x, fft_size)

w = np.arange(0, fft_size) * fs / fft_size

# 結果
fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(w, np.angle(X))
ax1.set_xlabel("frequency [Hz]")
ax1.set_ylabel("phase [rad]")
ax1.grid()

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(w, np.unwrap(np.angle(X)))
ax2.set_xlabel("frequency [Hz]")
ax2.set_ylabel("phase [rad]")
ax2.grid()

plt.tight_layout()

plt.show()
