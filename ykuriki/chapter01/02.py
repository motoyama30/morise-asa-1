import numpy as np
import matplotlib.pyplot as plt


x = np.array([1,3,-5,2])
y = np.array([[1],[3],[-5],[2]])

inner_product = np.dot(x,x)
print(inner_product)

inner_product = x @ x.T
print(inner_product)