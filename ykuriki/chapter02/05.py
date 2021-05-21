import numpy as np


fs = 100
t = np.arange(0, fs)/fs
f = 1
signal = np.sin(2*np.pi*f*t)
noise = np.random.randn(fs)

print(10*np.log10(sum(signal**2)))
print(10*np.log10(sum(noise**2)))

snr = 6
noise = noise/np.sqrt(sum(noise**2))
noise = noise*np.sqrt(sum(signal**2))
noise = noise*10**(-snr/20)

print(10*np.log10(np.mean(signal**2)/np.mean(noise**2)))