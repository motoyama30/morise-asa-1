import numpy as np

x = np.array([1,3,-5,2])
y = np.array([[1],[3],[-5],[2]])

print(x)
print(y)

inner_product = np.dot(x,y)
print(inner_product)
inner_product_T = np.dot(x,x.T)
print(inner_product_T)