# 直交関数列(orthogonal functions)の確認
import numpy as np

# 振幅rと位相θをパラメータとした1Hzの正弦波の生成
def CreateSound(fs,n,r,theta):
    t = np.arange(fs).reshape((fs, 1))/fs # (1,fs)の縦ベクトル
    x = r*np.cos(2*np.pi*n*t-theta)
    return t,x

def EstimateAB(fs,t,x,m):
    a = 2/fs*np.sum(x*np.cos(2*np.pi*m*t))
    b = 2/fs*np.sum(x*np.sin(2*np.pi*m*t))

    return a,b

if __name__ == '__main__':
    # 初期値
    fs = 44100
    r = 1.5
    theta = 0.3
    n = 2
    m = 3

    t,x = CreateSound(fs,n,r,theta)
    a,b = EstimateAB(fs,t,x,m)

    print(f'a : {a}')
    print(f'b : {b}')

    # フォーマットを変更する
    a_f = format(a, '.17f')
    b_f = format(b, '.17f')

    print(f'a : {a_f}')
    print(f'b : {b_f}')


