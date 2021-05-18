import numpy as np
import matplotlib.pyplot as plt

import sounddevice as sd

fs = 44100 # サンプリング周波数
f = 100 # 正弦波の周波数

t = np.arange(fs)/fs
x = np.sin(2*np.pi*f*t)

# 波形の再生
sd.play(x, fs)
status = sd.wait()

# 波形の表示
plt.plot(t, x)
plt.show()