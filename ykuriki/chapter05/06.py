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
N = round(fs * 0.02)
fft_size = 65536

win_han = MyHanning(N)
W_han = 20 * np.log10(
    abs(np.fft.fft(win_han, fft_size)),
    out=np.zeros_like(abs(np.fft.fft(win_han, fft_size))),
    where=(abs(np.fft.fft(win_han, fft_size) != 0)),
)
W_han = np.fft.fftshift(W_han) - max(W_han)

win_ham = MyHamming(N)
W_ham = 20 * np.log10(
    abs(np.fft.fft(win_ham, fft_size)),
    out=np.zeros_like(abs(np.fft.fft(win_ham, fft_size))),
    where=(abs(np.fft.fft(win_ham, fft_size) != 0)),
)
W_ham = np.fft.fftshift(W_ham) - max(W_ham)

win_bla = MyBlackman(N)
W_bla = 20 * np.log10(
    abs(np.fft.fft(win_bla, fft_size)),
    out=np.zeros_like(abs(np.fft.fft(win_bla, fft_size))),
    where=(abs(np.fft.fft(win_bla, fft_size) != 0)),
)
W_bla = np.fft.fftshift(W_bla) - max(W_bla)

w = np.arange(0, fft_size) / fft_size * fs - fs / 2

# プロット
plt.plot(w, W_han, label="hanning")
plt.plot(w, W_ham, label="hamming", ls="--")
plt.plot(w, W_bla, label="blackman", ls="-.")
plt.xlim(-400, 400)
plt.xlabel("frequency [Hz]")
plt.ylim(-80, 0)
plt.ylabel("power [dB]")
plt.grid()
plt.legend()

plt.show()
