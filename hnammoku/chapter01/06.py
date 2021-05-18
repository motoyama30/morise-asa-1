# 畳み込み演算
import numpy as np
x = [1,3,-5,2]
print(x)
h = [1,2,1]
print(h)
y = np.convolve(x, h)
print(y)