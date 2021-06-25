import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 8000
f1 = 3
f2 = 3.5

t = np.arange(0, fs) / fs
x1 = np.cos(2 * np.pi * f1 * t)
X1 = abs(np.fft.fft(x1)) / len(x1)
x2 = np.cos(2 * np.pi * f2 * t)
X2 = abs(np.fft.fft(x2)) / len(x2)

w = np.arange(0, len(t)) * fs / len(t)

# プロット
fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
ax1.stem(w, X1)
ax1.set_xlim(0, 10)
ax1.set_xlabel("frequency [Hz]")
ax1.set_ylabel("amplitude")
ax1.set_title("3 [Hz]")
ax1.grid()

ax2 = fig.add_subplot(2, 1, 2)
ax2.stem(w, X2)
ax2.set_xlim(0, 10)
ax2.set_xlabel("frequency [Hz]")
ax2.set_ylim(ax1.get_ylim())
ax2.set_ylabel("amplitude")
ax2.set_title("3.5 [Hz]")
ax2.grid()

plt.tight_layout()
plt.show()
