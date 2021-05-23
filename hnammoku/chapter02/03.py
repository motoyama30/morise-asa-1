# 信号のパワー比計算
import numpy as np

# 信号生成
N = 1000
x1 = np.random.randn(N, 1)
x2 = np.random.randn(N, 1)

# 直流成分除去
x1 = x1-np.mean(x1)
x2 = x2-np.mean(x2)

# パワー比計算
p1 = np.sum(x1**2)/N
p2 = np.sum(x2**2)/N
Lp = 10*np.log10(p1/p2)
print(Lp)