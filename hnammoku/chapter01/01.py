# 離散信号と波形表示
import matplotlib.pyplot as plt
import numpy as np
X = [1,3,-5,2]
plt.plot(X)
# 標本化周波数を10Hzに設定し、横軸を秒を単位とした時間軸として波形を表示
fs = 10
t = np.arange(len(X))/fs
plt.plot(t,X)
# ラベル追加
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")