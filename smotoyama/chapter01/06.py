import numpy as np

x = [1,3,-5,2]
h = [1,2,1];
y = np.convolve(x,h)

print(y)
