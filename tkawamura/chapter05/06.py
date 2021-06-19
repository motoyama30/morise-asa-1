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
N = int(np.round(fs * 0.02))
fft_size = 65536
win_han = MyHanning(N)
W_han = 20 * np.log10(
    np.maximum(np.fft.fftshift(np.abs(np.fft.fft(win_han, fft_size))), 10 ** -18)
)
W_han = W_han - np.max(W_han)  # 除算は対数とると減算になる

win_ham = MyHamming(N)
W_ham = 20 * np.log10(
    np.maximum(np.fft.fftshift(np.abs(np.fft.fft(win_ham, fft_size))), 10 ** -18)
)
W_ham = W_ham - np.max(W_ham)  # 除算は対数とると減算になる

win_bla = MyBlackman(N)
W_bla = 20 * np.log10(
    np.maximum(np.fft.fftshift(np.abs(np.fft.fft(win_bla, fft_size))), 10 ** -18)
)
W_bla = W_bla - np.max(W_bla)  # 除算は対数とると減算になる


w = np.arange(fft_size) * fs / fft_size - fs / 2
plt.plot(w, W_han)
plt.plot(w, W_ham, "--")
plt.plot(w, W_bla, "-.")
plt.xlim(-400, 400)
plt.ylim(-80, 0)
plt.show()
