import numpy as np
import matplotlib.pyplot as plt


def task4_2():
    # 定義
    fs = 44100
    t = np.arange(fs) / fs
    f = 5
    x = np.sin(2 * np.pi * f * t)
    fft_size = 2 ** np.math.ceil(np.log2(x.shape[0]))

    X1 = np.fft.fft(x)
    X2 = np.fft.fft(x, fft_size)

    w1 = np.arange(x.shape[0]) * fs / x.shape[0]
    w2 = np.arange(fft_size) * fs / fft_size

    # plot
    plt.plot(w1, np.abs(X1))
    plt.xlim(0, 50)
    # plt.show()
    plt.plot(w2, np.abs(X2))
    plt.xlim(0, 50)
    # plt.show()

    print("{}".format(np.sum(x ** 2)))
    print("{}".format(np.sum(np.abs(X1) ** 2 / X1.shape[0])))
    print("{}".format(np.sum(np.abs(X2) ** 2 / fft_size)))


if __name__ == "__main__":
    task4_2()
