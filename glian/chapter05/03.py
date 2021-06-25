import matplotlib.pyplot as plt
import numpy as np

def MyHanning(N):
    n = np.arange(N)
    win = (1 - np.cos(2 * np.pi * n / (N - 1))) / 2

    return win


def MyHamming(N):
    n = np.arange(N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))

    return win


def MyBlackman(N):
    n = np.arange(N)
    win = (
            0.42
            - 0.5 * np.cos(2 * np.pi * n / (N - 1))
            + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    )

    return win


fs = 44100
win_han = MyHanning(fs)
win_ham = MyHamming(fs)
win_bla = MyBlackman(fs)

t = np.arange(fs) / fs

plt.plot(t, win_han, label="Hanning window")
plt.plot(t, win_ham, "--", label="Hamming window")
plt.plot(t, win_bla, "-.", label="Blackman window")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.show()