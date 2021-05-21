import numpy as np
import matplotlib.pyplot as plt

# 信号の作成
fs = 100
t = np.arange(fs).reshape((fs, 1))/fs
f = 1
signal = np.sin(2*np.pi*f*t)
# パルス状の音源の作成
noise = np.zeros(fs).reshape((fs, 1))
number_of_pulses = 5
for i in range(number_of_pulses):
    noise[np.random.randint(len(noise))] = 2*round(np.random.rand())-1
# SNRが6
snr=6
noise=noise/np.sqrt(np.sum(noise**2)) # エネルギーの正規化
noise=noise*np.sqrt(np.sum(signal**2))
noise=noise*10**(-snr/20)
x = signal+noise # 混合音声の完成

# 06 移動平均フィルタ
y = np.zeros((len(x),1))
M = 5
for i in range(M+1,len(y)-M):
    y[i] = np.mean(x[i-M:i+M])

# 07 メディアンフィルタ (追加)
y_median = np.zeros((len(x),1))
M = 5
for i in range(M+1,len(y)-M):
    y_median[i] = np.median(x[i-M:i+M])

snr_in = 10*np.log10(np.sum(signal**2)/np.sum(noise**2))
snr_out = 10*np.log10(np.sum(signal**2)/np.sum((signal-y)**2))
snr_out_median = 10*np.log10(np.sum(signal**2)/np.sum((signal-y_median)**2))

print(f'input SNR : {snr_in}')
print(f'output SNR (moving average): {snr_out}')
print(f'output SNR (median): {snr_out_median}')



# グラフの表示(1)
plt.subplot(3,1,1)
plt.plot(t,x)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("x[n]:signal+noise ")

plt.subplot(3,1,2)
plt.plot(t,y)
plt.plot(t,signal,linestyle = "dashed",color = "orange")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("y[n](moving avarage)")

plt.subplot(3,1,3)
plt.plot(t,y_median)
plt.plot(t,signal,linestyle = "dashed",color = "orange")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("y[n](median filter)")

plt.tight_layout() # グラフタイトルが重ならないようにする
plt.show()
