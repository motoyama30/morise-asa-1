import numpy as np
import matplotlib.pyplot as plt


def analyze_spectrum_angle(fs, x, fft_size):
    t = np.arange(len(x))
    X = np.fft.fft(x, fft_size)
    Xd = np.fft.fft(-1j * t * x, fft_size)
    tau_d = (np.real(Xd) * np.imag(X) - np.real(X) * np.imag(Xd)) / abs(X) ** 2
    w = np.arange(fft_size) / fft_size * fs

    plt.plot(w, tau_d)
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
