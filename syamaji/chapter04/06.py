import numpy as np
import matplotlib.pyplot as plt


def task4_6():
    # 定義
    fs = 44100
    fft_size = 65536
    x = np.zeros(fft_size)
    x[1] = 1
    X = np.fft.fft(x, fft_size)
    w = np.arange(fft_size) / fft_size * fs

    # phase_delay = -np.unwrap(np.angle(X)) / (2 * np.pi * w)
    phase_delay = -np.unwrap(np.angle(X)) / (2 * np.pi * w)

    # plot
    plt.plot(w, phase_delay * fs)
    plt.grid()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    task4_6()
