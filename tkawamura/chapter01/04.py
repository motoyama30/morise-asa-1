import numpy as np

x = 3+4*1j
print(x)

r = np.abs(x)
theta = np.angle(x)
print("abs: {}, theta: {}".format(r, theta))

print(x.real)
print(x.imag)