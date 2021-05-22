# 正弦波の重ね合わせ
# 1Hz n1:1 r1:1.5 theta1:0.3
# 3Hz n2:3 r2:0.3 theta2:1.1
import numpy as np

# 正弦波を重ね合わせる
fs = 44100
n1 = 1
r1 = 1.5
theta1 = 0.3
n2 = 3
r2 = 0.3
theta2 = 1.1
t = np.arange(fs).reshape((fs, 1))/fs # (1,fs)の縦ベクトル
x = r1*np.cos(2*np.pi*n1*t-theta1) + r2*np.cos(2*np.pi*n2*t-theta2)

# a,bの計算(1Hzについて)
a = 2/fs*np.sum(x*np.cos(2*np.pi*t*n1))
b = 2/fs*np.sum(x*np.sin(2*np.pi*t*n1))

# 振幅と位相の取得
amplitude = np.sqrt(a**2+b**2)
phase = np.arctan2(b,a)
print(f'amplitude(1Hz) : {amplitude}')
print(f'phase(1Hz) : {phase}')

# a,bの計算(3Hzについて)
a_2 = 2/fs*np.sum(x*np.cos(2*np.pi*t*n2))
b_2 = 2/fs*np.sum(x*np.sin(2*np.pi*t*n2))

# 振幅と位相の取得
amplitude_2 = np.sqrt(a_2**2+b_2**2)
phase_2 = np.arctan2(b_2,a_2)
print(f'amplitude(3Hz) : {amplitude_2}')
print(f'phase(3Hz) : {phase_2}')