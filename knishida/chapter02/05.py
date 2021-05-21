import numpy as np


fs=100
t=np.arange(0,1,1/fs)
f=1

signal=np.array(np.sin(2*np.pi*f*t))
noise=np.random.randn(fs)

snr=6
noise=noise/np.sqrt(np.sum(noise**2))
noise=noise*np.sqrt(np.sum(signal**2))
noise=noise*10**(-snr/20)

p_sig=10*np.log10(np.sum(signal**2))
p_nis=10*np.log10(np.sum(noise**2))
snr_result=10*np.log10(np.sum(signal**2)/np.sum(noise**2))

print("power of signal:"+str(p_sig))
print("power of noise :"+str(p_nis))
print("SNratio:"+str(snr_result))