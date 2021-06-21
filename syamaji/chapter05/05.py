import numpy as np
import matplotlib.pyplot as plt


def task5_5():
    # 定義
    fs = 44100
    N = round(fs * 0.02)
    fft_size = 65536
    win_rect = np.ones(N)
    W_rec = np.fft.fftshift(np.abs(np.fft.fft(win_rect, fft_size)))
    W_rec = W_rec/np.max(W_rec)
    w = np.arange(fft_size)*fs / fft_size - fs/2

    # plot
    plt.subplot(2, 1, 1)
    plt.plot(w, W_rec)
    plt.xlim(-400, 400)
    plt.ylim(0, 1)

    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    task5_5()
