import numpy as np
import matplotlib.pyplot as plt
from numpy.random import standard_exponential


fs=100
t=np.arange(0,1,1/fs)
f=1

signal=np.array(np.sin(2*np.pi*f*t))

snr=6
noise=np.zeros(fs)
number_of_pulses=5
for i in range(number_of_pulses):
    noise[np.random.randint(len(noise))]=2*round(np.random.rand())-1

x=signal+noise

y=np.zeros(len(x))
M=5
for i in range(M+1,len(y)-M):
    y[i]=np.mean(x[i-M:i+M])

z=np.zeros(len(x))
M=5
for i in range(M+1,len(y)-M):
    z[i]=np.median(x[i-M:i+M])

snr_in=10*np.log10(np.sum(signal**2)/np.sum(noise**2))
snr_out_ave=10*np.log10(np.sum(signal**2)/np.sum((signal-y)**2))
snr_out_mdn=10*np.log10(np.sum(signal**2)/np.sum((signal-z)**2))

print("input  SNR:"+str(snr_in))
print("output SNR(moving average filter):"+str(snr_out_ave))
print("output SNR(median filter)"+str(snr_out_mdn))

ax1=plt.subplot(3,1,1)
ax2=plt.subplot(3,1,2)
ax3=plt.subplot(3,1,3)

ax1.plot(t,signal)
ax2.plot(t,y)
ax3.plot(t,z)

ax1.set_ylim(-2,2)
ax2.set_ylim(-2,2)
ax3.set_ylim(-2,2)

ax1.set_xlabel("Time[sample]")
ax1.set_ylabel("Amplitude")
ax2.set_xlabel("Time[sample]")
ax2.set_ylabel("Amplitude")
ax3.set_xlabel("Time[sample]")
ax3.set_ylabel("Amplitude")

ax1.set_title("signal")
ax2.set_title("estimated signal(moving average filter)")
ax3.set_title("estimated signal(median filter)")

plt.tight_layout()

plt.show()