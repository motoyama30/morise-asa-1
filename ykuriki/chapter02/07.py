import numpy as np
import matplotlib.pyplot as plt


fs = 100
t = np.arange(0, fs)/fs
f = 1
signal = np.sin(2*np.pi*f*t)

noise = np.zeros(fs)
number_of_pulses = 5
for i in range(0, number_of_pulses):
    noise[np.random.randint(0,len(noise))] = 2*round(np.random.rand())-1

snr = 6
noise = noise/np.sqrt(sum(noise**2))
noise = noise*np.sqrt(sum(signal**2))
noise = noise*10**(-snr/20)

x = signal+noise

y = np.zeros(len(x))
M = 5
for i in range(M, len(y)-M):
    y[i] = np.median(x[i-M:i+M])

##check
print(10*np.log10(np.mean(signal**2)/np.mean(noise**2)))
print(10*np.log10(np.mean(signal**2)/np.mean((y-signal)**2)))

plt.plot()
plt.plot(t, signal, label='signal')
plt.plot(t, x, ls='--', label='x')
plt.plot(t, y, ls='-.', label='y')
plt.show()