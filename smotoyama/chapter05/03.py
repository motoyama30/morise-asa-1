import numpy as np
import matplotlib.pyplot as plt


def MyHanning(N: int):
    n = np.arange(1, N + 1)
    win = (1 - np.cos(2 * np.pi * n / (N + 1))) / 2
    return win


def MyHamming(N: int):
    n = np.arange(N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return win


def MyBlackman(N: int):
    n = np.arange(N)
    win = (
        0.42
        - 0.5 * np.cos(2 * np.pi * n / (N - 1))
        + 0.8 * np.cos(4 * np.pi * n / (N - 1))
    )
    return win


fs = 44100
t = np.arange(fs) / fs

# cal
win_han = MyHanning(fs)
win_ham = MyHamming(fs)
win_bla = MyBlackman(fs)


# plot
plt.plot(t, win_han, label="Hanning window")
plt.plot(t, win_ham, ls="--", label="Hamming window")
plt.plot(t, win_bla, ls="-", label="Blackman window")
plt.xlabel("Time[s]")
plt.ylabel("振幅")
plt.grid()
plt.legend()
plt.show()
