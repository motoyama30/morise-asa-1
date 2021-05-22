# 高速フーリエ変換によるスペクトル解析
import numpy as np
import matplotlib.pyplot as plt
N = 8 # 信号長
#np.random.seed(0) # シード値
x = np.random.randn(N,1)
t = np.arange(N).reshape((N, 1))
x = np.sin(2*np.pi*2*t)
print(x)
print(x.shape)
print(x)
plt.plot(x)
plt.show()
c = np.zeros((N,1),dtype="complex128") # ゼロ埋めを行う(複素数範囲での配列の作成が必要)
t = np.arange(N).reshape((N, 1)) # (1,fs)の縦ベクトル
print(c)
# DFTでの値の計算
for i in range(N):
    c[i] = np.sum(x*np.exp(-1j*2*np.pi*i*t/N))
    print(np.sum(x*np.exp(-1j*2*np.pi*i*t))/N)



# FFT関数での値の計算
X = np.fft.fft(x)
print(X.dtype)
print(c)
print(X)
print(np.abs(c))
print(np.abs(X))

plt.subplot(2,1,1)
plt.plot(np.abs(c))
plt.subplot(2,1,2)
plt.plot(np.abs(X))
plt.show()
