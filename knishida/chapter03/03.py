import numpy as np


#declare
fs=44100
r=1.5
theta=0.3
n=2
m=3
t=np.arange(0,1,1/fs)
x=np.array(r*np.cos(2*np.pi*n*t-theta))

#calc about a,b
a=2/fs*np.sum(x*np.cos(2*np.pi*m*t))
b=2/fs*np.sum(x*np.sin(2*np.pi*m*t))

#output
print("a:"+str(a))
print("b:"+str(b))
