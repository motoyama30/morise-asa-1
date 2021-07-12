# 窓関数による処理
import numpy as np
import matplotlib.pyplot as plt

# ブラックマン窓生成
def MyBlackman(N):
    n = np.arange(N)
    win = (
        0.42
        - 0.5 * np.cos(2 * np.pi * n / (N - 1))
        + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    )
    return win


# 振幅スペクトルの設計
fs = 44100
fft_size = 65536
fc = 100
w = np.arange(fft_size) / fft_size * fs
fc_index = np.round(fft_size / fs * fc) + 1
amp_spec = np.ones(fft_size // 2 + 1)
amp_spec[int(fc_index) :] = 0

# インパルス応答の計算
spec = np.block([amp_spec, amp_spec[-2:0:-1]])
impulse_response = np.fft.fftshift(np.real(np.fft.ifft(spec)))
# 振幅特性の検証
fft_size2 = 65536 * 16
w2 = np.arange(fft_size2) / fft_size2 * fs

# 窓関数による処理
half_N = 32767
window_index = np.arange(fft_size // 2 - half_N, fft_size // 2 + half_N)
h = impulse_response[window_index] * MyBlackman(half_N * 2)

# グラフ描画
plt.plot(w2, np.abs(np.fft.fft(impulse_response, fft_size2)), ls="--", label="rect")
plt.plot(w2, np.abs(np.fft.fft(h, fft_size2)), ls="-", label="Blackman")
plt.xlim([90, 110])
plt.ylim([0, 1.2])
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.legend(loc="best")
plt.show()
