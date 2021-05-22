# 0Hzとナイキスト周波数の振幅の検証
import numpy as np

fs = 8

r = 0.5
t = np.arange(fs).reshape((fs, 1))/fs # (1,fs)の縦ベクトル
for i in range(5): # fを1から4まで検証する
    f = i
    x =  r*np.cos(2*np.pi*f*t)
    c = np.sum(x*np.exp(-1j*2*np.pi*f*t))/fs
    amplitude = np.abs(c)

    print(f'amplitude (f = {f}Hz): {amplitude}')
    # f = 4の時、振幅0.5になる