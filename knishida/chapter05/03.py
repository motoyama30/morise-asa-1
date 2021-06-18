import numpy as np
import matplotlib.pyplot as plt


# function
def MyHanning(N):
    n = np.arange(1, N + 1)
    win = (1 - np.cos(2 * np.pi * n / (N + 1))) / 2
    return win


def MyHamming(N):
    n = np.arange(0, N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return win


def MyBlackman(N):
    n = np.arange(0, N)
    win = (
        0.42
        - 0.5 * np.cos(2 * np.pi * n / (N - 1))
        + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    )
    return win


# declare
fs = 44100
win_han = MyHanning(fs)
win_ham = MyHamming(fs)
win_bla = MyBlackman(fs)
t = np.arange(0, 1, 1 / fs)

# output
plt.plot(t, win_han, linestyle="solid", label="Hanning window")
plt.plot(t, win_ham, linestyle="dashed", label="Hamming window")
plt.plot(t, win_bla, linestyle="dashdot", label="Blackman window")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
