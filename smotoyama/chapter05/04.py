import numpy as np


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
f = 1000
x = np.sin(2 * np.pi * f * t)
fft_size = 65536
w = np.arange(fft_size / 2 + 1) * fs / fft_size

# cal
X_han = np.fft.fft(x * MyHanning(len(x)), fft_size)
X_han = abs(X_han[0 : int(fft_size / 2) + 1])
spectal_centroid_han = np.sum(w * X_han) / np.sum(X_han)

X_ham = np.fft.fft(x * MyHamming(len(x)), fft_size)
X_ham = abs(X_ham[0 : int(fft_size / 2) + 1])
spectal_centroid_ham = np.sum(w * X_ham) / np.sum(X_ham)

X_bla = np.fft.fft(x * MyBlackman(len(x)), fft_size)
X_bla = abs(X_bla[0 : int(fft_size / 2) + 1])
spectal_centroid_bla = np.sum(w * X_bla) / np.sum(X_bla)

# output
print(spectal_centroid_han)
print(spectal_centroid_ham)
print(spectal_centroid_bla)
