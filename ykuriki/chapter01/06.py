import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 3, -5, 2])
h = np.array([1, 2, 1])
y = np.convolve(x, h)

print(y)
