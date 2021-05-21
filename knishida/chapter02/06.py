import numpy as np
import matplotlib.pyplot as plt
from numpy.random import standard_exponential


fs=100
t=np.arange(0,1,1/fs)
f=1

signal=np.array(np.sin(2*np.pi*f*t))
noise=np.random.randn(fs)

snr=6
noise=noise/np.sqrt(np.sum(noise**2))
noise=noise*np.sqrt(np.sum(signal**2))
noise=noise*10**(-snr/20)

x=signal+noise

y=np.zeros(len(x))
M=5
for i in range(M+1,len(y)-M):
    y[i]=np.mean(x[i-M:i+M])

snr_in=10*np.log10(np.sum(signal**2)/np.sum(noise**2))
snr_out=10*np.log10(np.sum(signal**2)/np.sum((signal-y)**2))

print("input  SNR:"+str(snr_in))
print("output SNR:"+str(snr_out))

ax1=plt.subplot(3,1,1)
ax2=plt.subplot(3,1,2)
ax3=plt.subplot(3,1,3)

ax1.plot(t,signal)
ax2.plot(t,x)
ax3.plot(t,y)

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
ax2.set_title("signal+noise")
ax3.set_title("estimated signal")

plt.tight_layout()

plt.show()