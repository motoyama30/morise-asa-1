import numpy as np 
import matplotlib.pyplot as plt

x = 3+4j
r = abs(x)
theta = np.angle(x)

print(r)
print(x.real)
print(x.imag)
print(theta)

