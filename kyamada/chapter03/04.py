# 正弦波の重ね合わせ
# 1Hz n1:1 r1:1.5 theta1:0.3
# 3Hz n2:3 r2:0.3 theta2:1.1
import numpy as np

# 正弦波を重ね合わせる
def CreateTwoSounds(fs,f1,r1,theta1,f2,r2,theta2):
    t = np.arange(fs).reshape((fs, 1))/fs # (1,fs)の縦ベクトル
    x = r1*np.cos(2*np.pi*f1*t-theta1) + r2*np.cos(2*np.pi*f2*t-theta2)
    return t,x

def EstimateAB(fs,t,x,n,message=None):
    # a,bの計算
    a = 2/fs*np.sum(x*np.cos(2*np.pi*t*n))
    b = 2/fs*np.sum(x*np.sin(2*np.pi*t*n))

    # 振幅と位相の取得
    amplitude = np.sqrt(a**2+b**2)
    phase = np.arctan2(b,a)
    print(f'amplitude {message} : {amplitude}')
    print(f'phase {message} : {phase}')

if __name__ == '__main__':
    fs = 44100
    n1 = 1
    r1 = 1.5
    theta1 = 0.3
    n2 = 3
    r2 = 0.3
    theta2 = 1.1

    t,x = CreateTwoSounds(fs,n1,r1,theta1,n2,r2,theta2)
    EstimateAB(fs,t,x,n1,message='(1Hz)')
    EstimateAB(fs,t,x,n2,message='(3Hz)')

