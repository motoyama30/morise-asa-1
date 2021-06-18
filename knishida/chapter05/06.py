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
N = np.round(fs * 0.02)
fft_size = 65536
win_han = MyHanning(int(N))
win_ham = MyHamming(int(N))
win_bla = MyBlackman(int(N))


# calc
W_han = 20 * np.log10(np.abs(np.fft.fft(win_han, fft_size)))
W_han = np.fft.fftshift(W_han) - np.max(W_han)

W_ham = 20 * np.log10(np.abs(np.fft.fft(win_ham, fft_size)))
W_ham = np.fft.fftshift(W_ham) - np.max(W_ham)

W_bla = 20 * np.log10(np.abs(np.fft.fft(win_bla, fft_size)))
W_bla = np.fft.fftshift(W_bla) - np.max(W_bla)

# output
w = np.arange(0, fft_size) / fft_size * fs - fs / 2
plt.plot(w, W_han, linestyle="solid", label="Hanning window")
plt.plot(w, W_ham, linestyle="dashed", label="Hamming window")
plt.plot(w, W_bla, linestyle="dashdot", label="Blackman window")
plt.xlim(-400, 400)
plt.ylim(-80, 0)
plt.xlabel("frequency [Hz]")
plt.ylabel("power [dB]")
plt.legend()
plt.show()
