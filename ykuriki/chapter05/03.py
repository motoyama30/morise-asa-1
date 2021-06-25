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

win_han = MyHanning(fs)
win_ham = MyHamming(fs)
win_bla = MyBlackman(fs)
t = np.arange(0, fs) / fs

# プロット
plt.plot(t, win_han, label="hanning")
plt.plot(t, win_ham, label="hamming", ls="--")
plt.plot(t, win_bla, label="blackman", ls="-.")
plt.xlabel("time [s]")
plt.ylabel("amplitude")
plt.grid()
plt.legend()

plt.show()
