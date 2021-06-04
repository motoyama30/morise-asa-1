import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 100
f = 1
number_of_pulses = 5
snr = 6
M = 5

t = np.arange(0, fs) / fs
signal = np.sin(2 * np.pi * f * t)

noise = np.zeros(fs)
for i in range(0, number_of_pulses):
    noise[np.random.randint(0, len(noise))] = 2 * round(np.random.rand()) - 1

noise = noise / np.sqrt(sum(noise ** 2))
noise = noise * np.sqrt(sum(signal ** 2))
noise = noise * 10 ** (-snr / 20)
x = signal + noise

y = np.zeros(len(x))
for i in range(M, len(y) - M):
    y[i] = np.median(x[i - M : i + M])

# check
print("input SNR :", 10 * np.log10(np.mean(signal ** 2) / np.mean(noise ** 2)))
print("output SNR:", 10 * np.log10(np.mean(signal ** 2) / np.mean((y - signal) ** 2)))

plt.plot()
plt.plot(t, signal, label="signal")
plt.plot(t, x, ls="--", label="x")
plt.plot(t, y, ls="-.", label="y")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
