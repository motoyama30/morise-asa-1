import numpy as np
import matplotlib.pyplot as plt


def task5_1():
    # 定義
    fs = 8000
    t = np.arange(fs) / fs
    f1 = 3
    f2 = 3.5

    x1 = np.cos(2 * np.pi * f1 * t)
    X1 = abs(np.fft.fft(x1))/x1.shape
    x2 = np.cos(2 * np.pi * f2 * t)
    X2 = abs(np.fft.fft(x2))/x2.shape

    w = np.arange(t.shape[0])*fs / t.shape[0]

    # plot
    plt.subplot(2, 1, 1)
    plt.plot(w, X1,  label='f=3')
    plt.xlim(0, 10)
    plt.legend()
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(w, X2, label='f=3.5')
    plt.xlim(0, 10)
    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    task5_1()
