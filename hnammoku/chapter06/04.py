# 振幅スペクトルに基づくFIRフィルタの設計
import numpy as np
import matplotlib.pyplot as plt

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

# グラフ描画
plt.plot(
    w,
    np.abs(np.fft.fft(impulse_response, fft_size)),
    marker="o",
    label="N = 2^16",
    ls="None",
)
plt.plot(w2, np.abs(np.fft.fft(impulse_response, fft_size2)), label="N = 2^20")
plt.xlim([95, 105])
plt.ylim([0, 1.2])
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.legend(loc="best")
plt.show()
