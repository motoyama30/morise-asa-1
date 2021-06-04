import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 44100
f = 5

t = np.arange(0, fs * 2) / fs
x = np.sin(2 * np.pi * f * t)
X = np.fft.fft(x)

w = np.arange(0, len(x)) * fs / len(x)

# 結果
plt.plot(w, abs(X))
plt.xlim(0, 50)
plt.xlabel("frequency [Hz]")
plt.ylabel("amplitude")
plt.grid()

plt.show()
