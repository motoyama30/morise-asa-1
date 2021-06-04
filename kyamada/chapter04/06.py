import numpy as np
import matplotlib.pyplot as plt


def analyze_spectrum_angle(fs, x, fft_size):
    X = np.fft.fft(x, fft_size)
    w = np.arange(fft_size) / fft_size * fs
    phase_delay = -np.unwrap(np.angle(X)) / (2 * np.pi * w)

    plt.plot(w, phase_delay * fs)
    plt.grid()
    plt.xlabel("frequency [Hz]")
    plt.ylabel("delay sample")

    plt.tight_layout()
    plt.show()


def delay_sound(x, m):
    x[m] = 1
    return x


if __name__ == "__main__":
    fs = 44100
    fft_size = 65536
    m = 1

    x = np.zeros(fft_size)
    x = delay_sound(x, m)
    analyze_spectrum_angle(fs, x, fft_size)
