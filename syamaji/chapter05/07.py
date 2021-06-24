import numpy as np
import matplotlib.pyplot as plt


def task5_7():
    # 定義
    fs = 8000
    T = 1
    f1 = 100
    f2 = 2000
    k = (f2-f1)/T
    t = np.arange(fs*T) / fs
    x = np.sin(2*np.pi*(f1*t+(k/2)*t**2))

    fft_size = 8000
    w = np.arange(fft_size)*fs / fft_size

    # plot
    plt.plot(w, 20*np.log10(np.abs(np.fft.fft(x, fft_size))))
    plt.xlim(0, 3000)

    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    task5_7()
