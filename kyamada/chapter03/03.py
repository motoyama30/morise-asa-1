# 直交関数列(orthogonal functions)の確認
import numpy as np

# 振幅rと位相θをパラメータとした1Hzの正弦波の生成
fs = 44100
r = 1.5
theta = 0.3
n = 2
m = 3
t = np.arange(fs).reshape((fs, 1))/fs # (1,fs)の縦ベクトル
x = r*np.cos(2*np.pi*n*t-theta)
print(np.sum(x*np.cos(2*np.pi*m*t))) #値が違う？？

a = 2/fs*np.sum(x*np.cos(2*np.pi*m*t))
b = 2/fs*np.sum(x*np.sin(2*np.pi*m*t))

print(f'a : {a}')
print(f'b : {b}')
