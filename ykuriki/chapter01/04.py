import numpy as np
import matplotlib.pyplot as plt


x = 3 + 4 * 1j
r = abs(x)
theta = np.angle(x)

print(r)
print(theta)

print(x.real)
print(x.imag)
