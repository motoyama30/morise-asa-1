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
W_han = 20*np.log10(np.abs(np.fft.fft(win_han, fft_size)))
W_han = np.fft.fftshift(W_han - np.max(W_han))

win_ham = MyHamming(N)
W_ham = 20*np.log10(np.abs(np.fft.fft(win_ham, fft_size)))
W_ham = np.fft.fftshift(W_ham - np.max(W_ham))

win_bla = MyBlackman(N)
W_bla = 20*np.log10(np.abs(np.fft.fft(win_bla, fft_size)))
W_bla = np.fft.fftshift(W_bla - np.max(W_bla))

w = np.arange(fft_size)*fs / fft_size - fs/2

w = np.arange(fft_size) * fs / fft_size - fs / 2
plt.plot(w, W_han, label = 'Hanning')
plt.plot(w, W_ham, "--",label = 'Hamming')
plt.plot(w, W_bla, "-.",label = 'Balckman')
plt.xlim(-400, 400)
plt.ylim(-80, 0)
plt.grid()
plt.legend()
plt.show()