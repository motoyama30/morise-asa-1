import numpy as np


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


def MyHamming(N):
    """ハミング窓を生成する

    Args:
        N (int): 窓の長さ

    Returns:
        ndarray: ハミング窓（float型1次元配列）

    """
    n = np.arange(0, N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return win


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
f = 1000
fft_size = 65536

t = np.arange(0, fs) / fs
x = np.sin(2 * np.pi * f * t)
w = np.arange(0, fft_size // 2 + 1) / fft_size * fs

X_han = np.fft.fft(x * MyHanning(len(x)), fft_size)
X_han = abs(X_han[: fft_size // 2 + 1])
spectal_centroid_han = sum(w * X_han) / sum(X_han)

X_ham = np.fft.fft(x * MyHamming(len(x)), fft_size)
X_ham = abs(X_ham[: fft_size // 2 + 1])
spectal_centroid_ham = sum(w * X_ham) / sum(X_ham)

X_bla = np.fft.fft(x * MyBlackman(len(x)), fft_size)
X_bla = abs(X_bla[: fft_size // 2 + 1])
spectal_centroid_bla = sum(w * X_bla) / sum(X_bla)

print(f"hanning : {spectal_centroid_han:.10f}")
print(f"hamming : {spectal_centroid_ham:.10f}")
print(f"blackman: {spectal_centroid_bla:.10f}")
