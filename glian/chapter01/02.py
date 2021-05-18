import numpy as np
import matplotlib.pyplot as plt

x = [1,3,5,-2]
x = np.array([1,3,-5,2])
y = np.array([[1],[3],[-5],[2]])
print(x,y)
print(x@y)
print(x@x.T)