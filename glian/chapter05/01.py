import matplotlib.pyplot as plt
import numpy as np

fs = 8000
t = np.arange(fs) / fs
f1 = 3
f2 = 3.5
x1 = np.cos(2 * np.pi * f1 * t)
X1 = np.abs(np.fft.fft(x1)) / np.size(x1)
x2 = np.cos(2 * np.pi * f2 * t)
X2 = np.abs(np.fft.fft(x2)) / np.size(x2)

w = np.arange(np.size(t)) * fs / np.size(t)

# 周波数3[Hz]のcos
plt.subplot(2, 1, 1)
plt.plot(w, X1,label = "f =3 [Hz]")
plt.grid()
plt.xlim(0, 10)
plt.ylim(0, 0.6)
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")

# 周波数3.5[Hz]のcos
plt.subplot(2, 1, 2)
plt.plot(w, X2, label = "f = 3.5 [Hz]")
plt.grid()
plt.xlim(0, 10)
plt.ylim(0, 0.6)
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()