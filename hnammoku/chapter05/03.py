# 窓関数の種類
import numpy as np
import matplotlib.pyplot as plt

# ハニング窓生成
def MyHanning(N):
    n = np.arange(N)
    win = (1 - np.cos(2 * np.pi * n / (N - 1))) / 2
    return win


# ハミング窓生成
def MyHamming(N):
    n = np.arange(N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return win


# ブラックマン窓生成
def MyBlackman(N):
    n = np.arange(N)
    win = (
        0.42
        - 0.5 * np.cos(2 * np.pi * n / (N - 1))
        + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    )
    return win


# 信号生成
fs = 44100
win_han = MyHanning(fs)
win_ham = MyHamming(fs)
win_bla = MyBlackman(fs)

# グラフ描画
t = np.arange(fs) / fs
plt.plot(t, win_han, label="Hanning window")
plt.plot(t, win_ham, "--", label="Hamming window")
plt.plot(t, win_bla, "-.", label="Blackman window")
plt.title("Shape of window functions")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
