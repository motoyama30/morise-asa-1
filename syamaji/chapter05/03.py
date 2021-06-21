import numpy as np
import matplotlib.pyplot as plt


def MyHanning(N):
    n = np.arange(N)
    win = (1-np.cos(2*np.pi*n/(N-1)))/2
    return win


def MyHamming(N):
    n = np.arange(N)
    win = 0.54 - 0.46*np.cos(2*np.pi*n/(N-1))
    return win


def MyBlackman(N):
    n = np.arange(N)
    win = 0.42 - 0.5*np.cos(2*np.pi*n/(N-1)) + 0.08*np.cos(4*np.pi*n/(N-1))
    return win


def task5_3():
    # 定義
    fs = 44100
    win_bla = MyBlackman(fs)
    win_ham = MyHamming(fs)
    win_han = MyHanning(fs)
    t = np.arange(fs) / fs

    # plot
    plt.subplot(2, 1, 1)
    plt.plot(t, win_han, 'k', label='Hanning')
    plt.plot(t, win_ham, 'k--', label='Hamming')
    plt.plot(t, win_bla, 'k-', label='Blackman')

    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    task5_3()
