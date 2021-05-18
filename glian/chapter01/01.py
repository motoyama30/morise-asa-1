import numpy as np
import matplotlib.pyplot as plt

x = [1,3,-5,2]
#plt.plot(x)
#plt.show()
#plt.close()
#np.arange(0,len)  = [0, 1, 2,..., len-1]
#横軸をサンプリング数 (0, 1, 2, 3) から時間(0s, 0.1s, 0.2s, 0.3s)へ変換
fs = 10
t = np.arange(len(x)) / fs
plt.plot(t,x)
#ラベル
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()