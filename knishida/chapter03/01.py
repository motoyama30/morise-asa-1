import numpy as np


#declare
fs=44100
t=np.arange(0,1,1/fs)
r=1.5
theta=0.3
x=np.array(r*np.cos(2*np.pi*t-theta))

#caluculate about a,b
a=2/fs*np.sum(x*np.cos(2*np.pi*t))
b=2/fs*np.sum(x*np.sin(2*np.pi*t))

#check
r_c=np.sqrt(a**2+b**2)
theta_c=np.arctan2(b,a)

#output
print("a:"+str(a))
print("b:"+str(b))
print("r:"+str(r_c))
print("theta:"+str(theta_c))
