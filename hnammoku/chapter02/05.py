# 信号と雑音の混合
import numpy as np
import matplotlib.pyplot as plt

# 信号とノイズの生成
fs = 1000
t = np.arange(fs)/fs
f = 1
signal = np.sin(2*np.pi*f*t)
noise = np.random.randn(fs, 1)
former = 10 * np.log10(np.sum(signal ** 2) / np.sum(noise ** 2))
# 各信号のパワー計算
ps = 10*np.log10(np.sum(signal**2))
pn = 10*np.log10(np.sum(noise**2))

# ノイズ更新
snr = 6
noise = noise*np.sqrt(np.sum(signal**2))/np.sqrt(np.sum(noise**2))*10**(-snr/20)
Lp = 10*np.log10(ps/pn)

# SNR計算
latter = 10 * np.log10(np.sum(signal ** 2) / np.sum(noise ** 2))
print('former_snr : {}'.format(former))
print('latter_snr : {}'.format(latter))
# 信号とノイズの混合
x = signal+noise

# グラフ表示
plt.subplot(2, 1, 1)
plt.title('signal')
plt.plot(t, signal)
plt.subplot(2, 1, 2)
plt.title('x')
plt.plot(t, x)
plt.show()