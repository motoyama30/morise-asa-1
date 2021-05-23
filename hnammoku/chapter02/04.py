# 平均時間・持続時間の計算
import numpy as np
import matplotlib.pyplot as plt

# 信号生成
fs = 41000
t = np.arange(fs)/fs
x = np.zeros(fs)
x[int(fs/2)-500+1:int(fs/2)+500+1] = 1

energy = np.sum(x**2)/fs
xx = x/np.sqrt(energy)
meantime = np.sum(t*xx**2)/fs
sigma1 = np.sum((t-meantime)**2*xx**2)/fs
sigma2 = np.sum(t**2*xx**2)/fs-meantime**2
sigma3 = (fs/np.sum(x**2))/3*(2*(500.5/fs)**3)

print('平均時間 : {}' .format(meantime))
print('eq1 : {}' .format(sigma1))
print('eq2 : {}' .format(sigma2))
print('eq3 : {}' .format(sigma3))

plt.plot(t, x)
plt.show()