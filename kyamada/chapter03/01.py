# パラメータ推定のプログラム
import numpy as np
import matplotlib.pyplot as plt

# 振幅rと位相θをパラメータとした1Hzの正弦波の生成
fs = 44100
r = 1.5
theta = 0.3
t = np.arange(fs).reshape((fs, 1))/fs # (1,fs)の縦ベクトル
x = r*np.cos(2*np.pi*t-theta)

# a,bの計算（式より）
a = 2/fs*np.sum(x*np.cos(2*np.pi*t)) # mTの代わりに計算結果が同じtを使う
b = 2/fs*np.sum(x*np.sin(2*np.pi*t))

# 振幅と位相の取得
amplitude = np.sqrt(a**2+b**2)
phase = np.arctan2(b,a)
print(f'amplitude : {amplitude}')
print(f'phase : {phase}')


