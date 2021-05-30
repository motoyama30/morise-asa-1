import numpy as np

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


# 確認を行う
# plt.plot(t,x)
# plt.show()
snr_check = 10 * np.log10(np.sum(signal ** 2) / np.sum(noise ** 2))
print(f"SNR check : {snr_check}")
