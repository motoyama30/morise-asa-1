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
t = np.arange(fs) / fs
f = 1000
x = np.sin(2 * np.pi * f * t)
fft_size = 65536
w = np.arange(fft_size // 2) * fs / fft_size

X_han = np.fft.fft(x * MyHanning(np.size(x)), fft_size)
X_han = np.abs(X_han[: fft_size // 2])
spectral_centroid_han = np.sum(w * X_han) / np.sum(X_han)

X_ham = np.fft.fft(x * MyHamming(np.size(x)), fft_size)
X_ham = np.abs(X_ham[: fft_size // 2])
spectral_centroid_ham = np.sum(w * X_ham) / np.sum(X_ham)

X_bla = np.fft.fft(x * MyBlackman(np.size(x)), fft_size)
X_bla = np.abs(X_bla[: fft_size // 2])
spectral_centroid_bla = np.sum(w * X_bla) / np.sum(X_bla)

print("Hanning window:  {}".format(spectral_centroid_han))
print("Hamming window:  {}".format(spectral_centroid_ham))
print("Blackman window: {}".format(spectral_centroid_bla))