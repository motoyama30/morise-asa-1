# 平均時間の算出
import numpy as np

# 信号生成
fs = 44100
N = 22050
x = np.random.randn(N)

# 時間信号から平均時間を算出
energy = np.sum(x ** 2) / fs
x = x / np.sqrt(energy)
t = np.arange(len(x)) / fs
t_c1 = np.sum(t * x ** 2) / fs

# スペクトルから平均時間を算出
fft_size = 2 ** np.ceil(np.log2(len(x)))
X = np.fft.fft(x, int(fft_size), axis=0)
Xd = np.fft.fft(-1j * t * x, int(fft_size), axis=0)
tau_d = (np.real(Xd) * np.imag(X) - np.real(X) * np.imag(Xd)) / np.abs(X) ** 2
t_c2 = np.sum(tau_d * np.abs(X) ** 2) / fs / fft_size

# 平均時間表示
print(f"時間信号から求めた平均時間：{t_c1:.20f}")
print(f"スペクトルから求めた平均時間：{t_c2:.20f}")
