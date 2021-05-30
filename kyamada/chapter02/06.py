import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
fs = 100
f = 1
snr = 6

# 信号の作成
t = np.arange(fs).reshape((fs, 1)) / fs
signal = np.sin(2 * np.pi * f * t)
# ホワイトノイズの作成
np.random.seed(0)  # シード値
noise = np.random.randn(fs, 1)

# パワーの計算を行う
signal_power = 10 * np.log10(np.sum(signal ** 2))
noise_power = 10 * np.log10(np.sum(noise ** 2))

print(f"power of signal : {signal_power}")
print(f"power of noise : {noise_power}")

# 混合をする
noise = noise / np.sqrt(np.sum(noise ** 2))  # エネルギーの正規化
noise = noise * np.sqrt(np.sum(signal ** 2))
noise = noise * 10 ** (-snr / 20)
x = signal + noise  # 混合音声の完成

# 06 移動平均フィルタ
y = np.zeros((len(x), 1))
M = 5
for i in range(M + 1, len(y) - M):
    y[i] = np.mean(x[i - M:i + M])

snr_in = 10 * np.log10(np.sum(signal ** 2) / np.sum(noise ** 2))
snr_out = 10 * np.log10(np.sum(signal ** 2) / np.sum((signal - y) ** 2))

print(f"input SNR : {snr_in}")
print(f"output SNR : {snr_out}")
# input SNR : 6.000000000000001
# output SNR : 15.363754909302354

# グラフの表示(1)
plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("s[n]:signal ")

plt.subplot(3, 1, 2)
plt.plot(t, x)
plt.plot(t, signal, linestyle="dashed", color="orange")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("x[n]:signal+noise")

plt.subplot(3, 1, 3)
plt.plot(t, y)
plt.plot(t, signal, linestyle="dashed", color="orange")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("y[n]")

plt.tight_layout()  # グラフタイトルが重ならないようにする
plt.show()
