import numpy as np


# パラメータ
fs = 100
f = 1
snr = 6

t = np.arange(0, fs) / fs
signal = np.sin(2 * np.pi * f * t)
noise = np.random.randn(fs)

print("power of signal:", 10 * np.log10(sum(signal ** 2)))
print("power of signal:", 10 * np.log10(sum(noise ** 2)))

noise = noise / np.sqrt(sum(noise ** 2))
noise = noise * np.sqrt(sum(signal ** 2))
noise = noise * 10 ** (-snr / 20)

print("SNR            :", 10 * np.log10(np.mean(signal ** 2) / np.mean(noise ** 2)))
