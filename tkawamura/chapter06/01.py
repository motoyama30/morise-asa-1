import numpy as np
import soundfile as sf

fs = 44100

x = np.random.randn(fs)  # 入力（ホワイトノイズ）
y = np.zeros(fs)  # 処理音声

y[0] = 0.5 * x[0]
for n in range(1, x.size):
    y[n] = 0.5 * x[n] - 0.5 * x[n - 1]

sf.write("./input.wav", x, fs)
sf.write("./output.wav", y, fs)
