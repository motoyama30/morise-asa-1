import numpy as np

x = np.array([1, 3, -5, 2])
y = np.array([[1], [3], [-5], [2]])

x = np.array([1, 3, -5, 2])
y = np.array([1, 3, -5, 2])

inner_product = np.sum(x*y)
print(inner_product)

inner_product = x @ y
print(inner_product)