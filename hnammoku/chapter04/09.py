# 持続時間の算出
import numpy as np

# 信号生成
fs = 44100
N = 22050
x = np.random.randn(N)

# 時間信号から持続時間を算出
energy = np.sum(x ** 2) / fs
x = x / np.sqrt(energy)
t = np.arange(len(x)) / fs
t_c = np.sum(t * x ** 2) / fs
sigma_t1 = np.sum((t - t_c) ** 2 * x ** 2) / fs

# スペクトルから持続時間を算出
fft_size = 2 ** np.ceil(np.log2(len(x)))
X = np.fft.fft(x, int(fft_size), axis=0)
Xd = np.fft.fft(-1j * t * x, int(fft_size), axis=0)
tau_d = (np.real(Xd) * np.imag(X) - np.real(X) * np.imag(Xd)) / np.abs(X) ** 2
d1 = ((np.real(X) * np.real(Xd) + np.imag(X) * np.imag(Xd)) / np.abs(X)) ** 2
d2 = (-tau_d + t_c) ** 2 * np.abs(X) ** 2
sigma_t2 = (np.sum(d1) + np.sum(d2)) / fft_size / fs

# 持続時間表示
print(f"時間信号から求めた平均時間：{sigma_t1:.20f}")
print(f"スペクトルから求めた平均時間：{sigma_t2:.20f}")
