import numpy as np
from func import MyHanning, MyHamming, MyBlackman
import matplotlib.pyplot as plt


def task5_6():
    # 定義
    fs = 44100
    N = round(fs * 0.02)
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

    # plot
    plt.plot(w, W_han, 'k', label='Hanning')
    plt.plot(w, W_ham, 'k--', label='Hamming')
    plt.plot(w, W_bla, 'k-', label='Blackman')

    plt.xlim(-400, 400)
    plt.ylim(-80, 0)

    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    task5_6()
