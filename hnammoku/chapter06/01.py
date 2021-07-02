# 差分方程式の実装
import numpy as np
import sounddevice as sd

# 信号生成
fs = 44100
x = np.random.randn(fs)
y = np.zeros(fs)

# 差分方程式
y[0] = 0.5 * x[0]
for n in range(1, fs):
    y[n] = 0.5 * x[n] - 0.5 * x[n - 1]

# 信号再生
sd.play(x)
sd.wait()

sd.play(y)
sd.wait()
