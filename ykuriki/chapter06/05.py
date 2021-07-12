import numpy as np
import matplotlib.pyplot as plt

# 関数
def MyBlackman(N):
    """ブラックマン窓を生成する

    Args:
        N (int): 窓の長さ

    Returns:
        ndarray: ブラックマン窓（float型1次元配列）

    """
    n = np.arange(0, N)
    win = (
        0.42
        - 0.5 * np.cos(2 * np.pi * n / (N - 1))
        + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    )
    return win


# パラメータ
fs = 44100
fft_size = 65536
fc = 100
fft_size2 = 65536 * 16
half_N = 32767

fc_index = round(fft_size * fc / fs) + 1
amp_spec = np.ones(fft_size // 2 + 1)
amp_spec[fc_index:] = 0

spec = np.block([amp_spec, amp_spec[-2:0:-1]])
impulse_response = np.fft.fftshift(np.fft.ifft(spec).real)

w2 = np.arange(0, fft_size2) / fft_size2 * fs

window_index = (
    np.arange(fft_size / 2 - half_N, fft_size / 2 + half_N + 1, dtype=int) + 1
)
h = impulse_response[window_index - 1] * MyBlackman(half_N * 2 + 1)

plt.plot(w2, abs(np.fft.fft(h, fft_size2)), color="k")
plt.plot(w2, abs(np.fft.fft(impulse_response, fft_size2)), color="k", ls="--")
plt.xlim(90, 110)
plt.xlabel("frequency [Hz]")
plt.ylabel("amplitude")
plt.show()
