import numpy as np

x = [1,3,-5,2]
h = [1,2,1]
#畳み込み関数
y = np.convolve(x, h)
print(y)