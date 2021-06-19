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
N = np.round(fs * 0.02)
fft_size = 65536
w = np.arange(fft_size) / fft_size * fs - fs / 2

# cal
win_han = MyHanning(N)
W_han = 20 * np.log10(abs(np.fft.fft(win_han, fft_size)))
W_han = np.fft.fftshift(W_han) - np.max(W_han)

win_ham = MyHamming(N)
W_ham = 20 * np.log10(abs(np.fft.fft(win_ham, fft_size)))
W_ham = np.fft.fftshift(W_ham) - np.max(W_ham)

win_bla = MyBlackman(N)
W_bla = 20 * np.log10(abs(np.fft.fft(win_bla, fft_size)))
W_bla = np.fft.fftshift(W_bla) - np.max(W_bla)

# plot
plt.plot(w, W_han, label="Hanning")
plt.plot(w, W_ham, ls="--", label="Hamming")
plt.plot(w, W_bla, ls="-", label="Blackman")
plt.xlim(-400, 400)
plt.ylim(0, 1)
plt.xlabel("周波数[Hz]")
plt.ylabel("相対パワー[dB]")
plt.legend()
plt.grid()
plt.show()
