import numpy as np


<<<<<<< HEAD
# パラメータ
=======
##パラメータ
>>>>>>> ade158846085480320c13d37c2b26953dd679278
fs = 44100
f1 = 1
r1 = 1.5
theta1 = 0.3
f2 = 3
r2 = 0.2
theta2 = -1.1

<<<<<<< HEAD
t = np.arange(0, fs) / fs
x = r1 * np.cos(2 * np.pi * f1 * t - theta1) + r2 * np.cos(2 * np.pi * f2 * t - theta2)

k1 = 1
c1 = sum(x * np.exp(-1j * 2 * np.pi * k1 * t)) / fs
k3 = 3
c3 = sum(x * np.exp(-1j * 2 * np.pi * k3 * t)) / fs

print("1[Hz]")
print("amplitude: {:.10f}".format(abs(c1)))
print("phase    : {:.10f}".format(np.angle(c1.conjugate())))
print("3[Hz]")
print("amplitude: {:.10f}".format(abs(c3)))
print("phase    : {:.10f}".format(np.angle(c3.conjugate())))
=======
t = np.arange(0,fs)/fs
x = r1*np.cos(2*np.pi*f1*t-theta1)+r2*np.cos(2*np.pi*f2*t-theta2)

k1 = 1
c1 = sum(x*np.exp(-1j*2*np.pi*k1*t))/fs
k3 = 3
c3 = sum(x*np.exp(-1j*2*np.pi*k3*t))/fs

print('1[Hz]')
print('amplitude: {:.10f}'.format(abs(c1)))
print('phase    : {:.10f}'.format(np.angle(c1.conjugate())))
print('3[Hz]')
print('amplitude: {:.10f}'.format(abs(c3)))
print('phase    : {:.10f}'.format(np.angle(c3.conjugate())))
>>>>>>> ade158846085480320c13d37c2b26953dd679278
