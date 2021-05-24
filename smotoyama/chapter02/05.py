import numpy as np
import matplotlib.pyplot as plt

fs = 100
t = np.arange(fs)/fs
f = 1

signal = np.sin(2*np.pi*f*t)
noise = np.random.randn(fs,1)

snr = 6

noise = noise/np.sqrt(np.sum(noise**2))
noise = noise*np.sqrt(np.sum(signal**2))
noise = noise*10**(-snr/20)

print(10*np.log10(sum(signal**2)/sum(noise**2)))