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


def MinimumPhase(x):
    """最小位相応答を求める

    Args:
        x (ndarray): インパルス応答

    Returns:
        ndarray: 最小位相応答

    """
    x_len_half = int(len(x) / 2 - 1)
    X = np.fft.ifft(np.log(abs(np.fft.fft(x)))).real
    w = np.block([1, 2 * np.ones(x_len_half), 1, np.zeros(x_len_half)])
    y = np.fft.ifft(np.exp(np.fft.fft(w * X))).real
    return y


# パラメータ
fs = 44100
fft_size = 65536
fc = 100
fft_size2 = 65536 * 16

w = np.arange(0, fft_size) / fft_size * fs
fc_index = round(fft_size * fc / fs) + 1
amp_spec = np.ones(fft_size // 2 + 1)
amp_spec[fc_index:] = 0.01
spec = np.block([amp_spec, amp_spec[-2:0:-1]])
impulse_response = np.fft.fftshift(np.fft.ifft(spec).real)
impulse_response[0] = 0
impulse_response[1:fft_size] = impulse_response[1:fft_size] * MyBlackman(fft_size - 1)
minimum_phase_response = MinimumPhase(impulse_response)

# プロット
plt.plot(np.arange(0, fft_size) / fs, minimum_phase_response)
plt.xlabel("time [s]")
plt.ylabel("amplitude")
plt.tight_layout()


w2 = np.arange(0, fft_size2) / fft_size2 * fs

# プロット
plt.figure()
plt.plot(
    w2, abs(np.fft.fft(impulse_response, fft_size2)), label="zero phase", color="k"
)
plt.plot(
    w2,
    abs(np.fft.fft(minimum_phase_response, fft_size2)),
    label="minimum phase",
    color="k",
    ls="--",
)
plt.xlim(95, 105)
plt.xlabel("frequency [Hz]")
plt.ylabel("amplitude")
plt.legend()
plt.grid()

plt.show()
