import numpy as np
import matplotlib.pyplot as plt


def task6_2():
    # 定義
    fs = 44100
    fft_size = 65536

    # plot
    plt.plot(w / 1000, abs(np.fft.fft(np.array([0.5, -0.5]), fft_size)))
    plt.xlim(0, fs/2000)

    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    task6_2()
