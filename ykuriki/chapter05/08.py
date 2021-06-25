import numpy as np
import matplotlib.pyplot as plt


# 関数
def MyHanning(N):
    """ハニング窓を生成する

    Args:
        N (int): 窓の長さ

    Returns:
        ndarray: ハニング窓（float型1次元配列）

    """
    n = np.arange(1, N + 1)
    win = (1 - np.cos(2 * np.pi * n / (N + 1))) / 2
    return win


# パラメータ
fs = 8000
T = 1
f1 = 100
f2 = 2000

k = (f2 - f1) / T
t = np.arange(0, fs * T) / fs
x = np.sin(2 * np.pi * (f1 * t + (k / 2) * t ** 2))

win_len = round(fs * 0.02)
win = MyHanning(win_len)
fft_size = 2 ** int(np.ceil(np.log2(win_len)))
frame_shift = round(fs * 0.01)
number_of_frames = int(np.ceil((len(x) + 1) / frame_shift))
X = np.zeros([fft_size // 2 + 1, number_of_frames])
base_index = np.arange(np.ceil(-win_len / 2), np.ceil(win_len / 2), dtype=int)

for i in range(0, number_of_frames):
    center = round(i * frame_shift)
    safe_index = np.where(
        np.where(base_index + center < len(x), base_index + center, len(x)) > 1,
        np.where(base_index + center < len(x), base_index + center, len(x)),
        1,
    )
    tmp = x[safe_index - 1] * win
    tmpX = 20 * np.log10(abs(np.fft.fft(tmp, fft_size)))
    X[:, i] = tmpX[: fft_size // 2 + 1]

# プロット
plt.imshow(
    np.where(X > X.max() - 60, X, X.max() - 60),
    cmap="gray",
    origin="lower",
    extent=[0, 1, 0, 4000],
    aspect="auto",
)
plt.xlabel("time [s]")
plt.ylabel("amplitude [Hz]")
plt.colorbar()

plt.show()
