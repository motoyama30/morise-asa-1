import numpy as np
import matplotlib.pyplot as plt


def task5_2():
    # 定義
    fs = 8000
    t = np.arange(fs) / fs
    f1 = 3
    f2 = 3.5
    fft_size = 2**17

    x1 = np.cos(2 * np.pi * f1 * t)
    X1 = abs(np.fft.fft(x1, fft_size))/x1.shape[0]
    x2 = np.cos(2 * np.pi * f2 * t)
    X2 = abs(np.fft.fft(x2, fft_size))/x2.shape[0]

    w = np.arange(fft_size)*fs / fft_size

    # plot
    plt.subplot(2, 1, 1)
    plt.plot(w, X1, 'k--', label='f=3')
    plt.xlim(0, 10)
    plt.legend()
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(w, X2, 'k--', label='f=3.5')
    plt.xlim(0, 10)
    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    task5_2()
