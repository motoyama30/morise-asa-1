# 周期の拡張(1秒→任意の周期への拡張)
import numpy as np
import matplotlib.pyplot as plt

# 振幅rと位相θをパラメータとした1Hzの正弦波の生成
def CreateSound(fs,f,r,theta,L):
    array_size = int(fs*L) # メモ：そのまま計算するとfloat型になるためキャストする必要がある
    t = np.arange(array_size).reshape((array_size, 1))/fs # (1,fs*L)の縦ベクトル
    x=r*np.cos(2*np.pi*t/L-theta)
    return t,x

def EstimateAB(fs,t,x):
    # a,bの計算（式より）
    a = 2/fs/L*np.sum(x*np.cos(2*np.pi*t/L))
    b = 2/fs/L*np.sum(x*np.sin(2*np.pi*t/L))

    # 振幅と位相の取得
    amplitude = np.sqrt(a**2+b**2)
    phase = np.arctan2(b,a)
    return amplitude,phase

if __name__=='__main__':
    fs = 44100
    f = 2
    r = 1.5
    theta = 0.3
    L = 1/f # 周期について追加

    t,x = CreateSound(fs,f,r,theta,L)
    amplitude,phase = EstimateAB(fs,t,x)

    print(f'amplitude : {amplitude}')
    print(f'phase : {phase}')