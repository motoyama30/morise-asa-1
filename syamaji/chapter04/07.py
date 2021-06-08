import numpy as np
import matplotlib.pyplot as plt


def task4_7():
    # 定義
    fs = 44100
    fft_size = 65536
    x = np.zeros(fft_size)
    x[1] = 1
    t = np.arange(x.shape[0])
    X = np.fft.fft(x, fft_size)
    Xd = np.fft.fft(-1j * t * x, fft_size)

    tau_d = (np.real(Xd) * np.imag(X) - np.real(X) * np.imag(Xd)) / np.abs(X) ** 2
    w = np.arange(fft_size) / fft_size * fs

    # plot
    print(tau_d)
    plt.plot(w, tau_d)
    plt.grid()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    task4_7()
