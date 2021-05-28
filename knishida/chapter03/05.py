import numpy as np


#declare
fs=44100
n1=1
r1=1.5
theta1=0.3
n2=3
r2=0.2
theta2=-1.1
t=np.arange(0,1,1/fs)
x=np.array(r1*np.cos(2*np.pi*n1*t-theta1)+r2*np.cos(2*np.pi*n2*t-theta2))

#calc about c
k1=1
c1=np.sum(x*np.exp(-1j*2*np.pi*k1*t))/fs
k3=3
c3=np.sum(x*np.exp(-1j*2*np.pi*k3*t))/fs

#check
r1_c=np.abs(c1)
theta1_c=np.angle(np.conj(c1))
r2_c=np.abs(c3)
theta2_c=np.angle(np.conj(c3))

#output
print("r1:"+str(r1_c))
print("theta1:"+str(theta1_c))
print("r2:"+str(r2_c))
print("theta2:"+str(theta2_c))
