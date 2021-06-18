import numpy as np
import matplotlib.pyplot as plt


def task4_5():
    # 定義
    fs = 8000
    x = np.zeros(fs)
    m = 1
    x[1 + m] = 1
    fft_size = 2 ** np.math.ceil(np.log2(x.shape[0]))
    X = np.fft.fft(x, fft_size)
    w = np.arange(fft_size) / fft_size * fs

    # plot
    plt.plot(w, np.angle(X))
    plt.plot(w, np.unwrap(np.angle(X)))
    plt.show()


if __name__ == "__main__":

    task4_5()
