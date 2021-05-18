import numpy as np

x = 3 + 3*1j #(3+4j)

print(abs(x))
print(x.imag)
theta = np.degrees(np.angle(x))
print(theta)
# read onlyなので変更はできない
# c.real = 5.5
# AttributeError: readonly attribute

#共役


