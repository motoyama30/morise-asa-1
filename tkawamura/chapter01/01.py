import numpy as np
import matplotlib.pyplot as plt

# 波形の表示
x = np.array([1, 3, -5, 2])
plt.plot(x)
plt.show()

# 波形の描画
fs = 10 # サンプリング周波数
t = np.arange(len(x))/fs
plt.plot(t, x)

# ラベルの追加
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()