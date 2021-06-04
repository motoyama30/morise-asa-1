import matplotlib.pyplot as plt
import numpy as np

fs = 44100
t = np.arange(fs * 2).reshape(fs * 2, 1) / fs  # 信号長が1秒分
f = 5
x = np.sin(2 * np.pi * f * t)
X = np.fft.fft(x, axis=0)
w = np.arange(len(x)).reshape(len(x), 1) * fs / len(x)

plt.plot(w, np.abs(X))
plt.xlim(0, 50)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.show()
