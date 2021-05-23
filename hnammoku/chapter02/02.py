# 正弦波の波形比較
import numpy as np
import matplotlib.pyplot as plt

# 正弦波の生成
fs = 10
n = np.arange(fs)
T = n*fs
f = 1
omega = 2*np.pi/fs
x1 = np.sin(omega*n)
x2 = np.sin((omega+2*np.pi)*n)

# グラフ表示
plt.subplot(2, 1, 1)
plt.plot(n, x1)
plt.title('sin(ωn)')
plt.subplot(2, 1, 2)
plt.plot(n, x2)
plt.title('sin( (ω+2π) n)')
plt.show()