import numpy as np
import matplotlib.pyplot as plt


def task4_4():
    # 定義
    fs = 44100
    t = np.arange(fs) / fs
    f = 5
    x = np.sin(2 * np.pi * f * t)
    X = np.fft.fft(x)

    w = np.arange(x.shape[0]) / x.shape[0] * fs

    # plot
    plt.plot(w, np.abs(X))
    plt.xlim(0, 50)
    plt.show()


if __name__ == "__main__":

    task4_4()
