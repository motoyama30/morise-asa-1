import numpy as np
import matplotlib.pyplot as plt

fs = 44100
t = np.arange(fs * 2) / fs
f = 5
x = np.sin(2 * np.pi * f * t)

# cul
X = np.fft.fft(x)
w = np.arange(len(x)) * fs / len(x)

# plot
plt.plot(w, abs(X))
plt.xlabel("周波数")
plt.ylabel("振幅スペクトル")
plt.grid()
plt.xlim(0, 50)
