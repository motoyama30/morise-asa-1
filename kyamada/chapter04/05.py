import numpy as np
import matplotlib.pyplot as plt


def create_sound(fs, f):
    t = np.arange(fs * 2) / fs
    x = np.sin(2 * np.pi * f * t)
    return t, x


def zero_padding(x):
    fft_size = 2 ** (np.ceil(np.log2(len(x))))
    return int(fft_size)


def analyze_spectrum_angle(fs, x, fft_size):
    X = np.fft.fft(x, fft_size)
    w = np.arange(fft_size) * fs / fft_size
    plt.subplot(2, 1, 1)
    plt.plot(w, np.angle(X))
    plt.grid()
    plt.xlabel("frequency [Hz]")
    plt.ylabel("angle [rad]")

    plt.subplot(2, 1, 2)
    plt.plot(w, np.unwrap(np.angle(X)))
    plt.grid()
    plt.xlabel("frequency [Hz]")
    plt.ylabel("angle [rad]")

    plt.tight_layout()
    plt.show()


def delay_sound(x, m):
    x[m] = 1
    return x


if __name__ == "__main__":
    fs = 8000
    m = 1
    x = np.zeros(fs)
    x = delay_sound(x, m)

    fft_size = zero_padding(x)
    analyze_spectrum_angle(fs, x, fft_size)
