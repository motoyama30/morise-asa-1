# 最小位相によるフィルタ設計
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


# 最小位相応答の計算
def MinimumPhase(x):
    x_len_half = int(len(x) / 2 - 1)
    X = np.real(np.fft.ifft(np.log(np.abs(np.fft.fft(x[:])))))
    w = np.block([1, 2 * np.ones(x_len_half), 1, np.zeros(x_len_half)])
    y = np.real(np.fft.ifft(np.exp(np.fft.fft(w * X))))
    return y


# 低域通過フィルタの実装
fs = 44100
fft_size = 65536
fc = 100
w = np.arange(fft_size) / fft_size * fs
fc_index = int(np.round(fft_size / fs * fc))
amp_spec = np.ones(fft_size // 2 + 1)
amp_spec[fc_index + 1 :] = 0.01
spec = np.block([amp_spec, amp_spec[-2:0:-1]])
impulse_response = np.fft.fftshift(np.real(np.fft.ifft(spec)))
impulse_response[0] = 0
impulse_response[1:fft_size] = impulse_response[1:fft_size] * MyBlackman(fft_size - 1)

# インパルス応答の表示
minimum_phase_response = MinimumPhase(impulse_response)
plt.subplot(2, 1, 1)
plt.plot(np.arange(fft_size) / fs, minimum_phase_response)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# 振幅の振る舞いの確認
fft_size2 = 65536 * 16
w2 = np.arange(fft_size2) / fft_size2 * fs
plt.subplot(2, 1, 2)
plt.plot(w2, np.abs(np.fft.fft(impulse_response, fft_size2)), ls="-", label="zero")
plt.plot(
    w2, np.abs(np.fft.fft(minimum_phase_response, fft_size2)), ls="--", label="minimum"
)
plt.xlim([95, 105])
plt.ylim([0, 1.2])
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")

plt.legend(loc="best")
plt.show()
