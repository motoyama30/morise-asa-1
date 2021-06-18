import numpy as np
import matplotlib.pyplot as plt


def my_hanning(N):
    n = np.arange(N)
    win = (1 - np.cos(2 * np.pi * n / (N + 1))) / 2
    return win


def my_hamming(N):
    n = np.arange(N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N + 1))
    return win


def my_blackman(N):
    n = np.arange(N)
    win = (
        0.42
        - 0.5 * np.cos(2 * np.pi * n / (N + 1))
        + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    )
    return win


if __name__ == "__main__":
    fs = 44100
    win_han = my_hanning(fs)
    win_ham = my_hamming(fs)
    win_bla = my_blackman(fs)
    t = np.arange(fs) / fs

    plt.plot(t, win_han, linestyle="solid", label="Hanning window")
    plt.plot(t, win_ham, linestyle="dashed", label="Hamming window")
    plt.plot(t, win_bla, linestyle="dashdot", label="Blackman window")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()
