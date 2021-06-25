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


def clc_power_spectre_wind(N, fft_size, fs, wind):
    win = wind
    W = 20 * np.log10(np.abs(np.fft.fft(win, fft_size)))
    W = np.fft.fftshift(W) - max(W)
    return W


if __name__ == "__main__":
    fs = 44100
    fft_size = 65536

    N = np.round(fs * 0.02)  # 四捨五入を行う
    W_han = clc_power_spectre_wind(N, fft_size, fs, my_hanning(int(N)))
    W_ham = clc_power_spectre_wind(N, fft_size, fs, my_hamming(int(N)))
    W_bla = clc_power_spectre_wind(N, fft_size, fs, my_blackman(int(N)))

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
