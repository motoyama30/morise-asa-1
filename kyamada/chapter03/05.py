# ckを導出する
import numpy as np

# 重ね合わせの信号xを生成
# 
# 
fs = 44100
f1 = 1
r1 = 1.5
theta1 = 0.3
f2 = 3
r2 = 0.2
theta2 = -1.1
t = np.arange(fs).reshape((fs, 1))/fs # (1,fs)の縦ベクトル
x = r1*np.cos(2*np.pi*f1*t-theta1) + r2*np.cos(2*np.pi*f2*t-theta2)

# k=1Hz,k=3Hzの時のckを導出する
k1 = 1
c1 = np.sum(x*np.exp(-1j*2*np.pi*k1*t))/fs

k3 = 3
c3 = np.sum(x*np.exp(-1j*2*np.pi*k3*t))/fs
print(f'ck(k=3) : {c3}')

# 振幅と位相を計算する
# k = 1のとき
amplitude1 = np.abs(c1) # 絶対値を取得
phase1 = np.angle(np.conj(c1)) # np.conj()で複素共役を取得
phase1_raku = np.angle(c1) # 負号が含まれる形ならnp.conjを省略できる


print(f'amplitude from ck (k=1) : {amplitude1}') # 振幅なのでr1の半分の値が出てくる
print(f'phase from ck (k=1): {phase1}') # 位相
print(f'phase from ck (k=1): {phase1_raku}')

# k = 3の時
amplitude3 = np.abs(c3) # 絶対値を取得
phase3 = np.angle(np.conj(c3)) # np.conj()で複素共役を取得
phase3_raku = np.angle(c3) # 負号が含まれる形ならnp.conjを省略できる


print(f'amplitude from ck (k=3) : {amplitude3}') # 振幅なのでr1の半分の値が出てくる
print(f'phase from ck (k=3): {phase3}') # 位相
print(f'phase from ck (k=3): {phase3_raku}')