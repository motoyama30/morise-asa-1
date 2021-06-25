import numpy as np
import matplotlib.pyplot as plt


def create_cos_wave(f, fs):
    t = np.arange(fs) / fs
    x = np.cos(2 * np.pi * f * t)
    return t, x


def cut_by_wind(t, x):
    X = np.abs(np.fft.fft(x)) / len(x)
    w = np.arange(0, len(t)) * fs / len(t)
    return X, w


def cut_by_wind_fftsize(t, x, fft_size):
    X = np.abs(np.fft.fft(x, fft_size)) / len(x)
    w = np.arange(0, fft_size) * fs / fft_size
    return X, w


if __name__ == "__main__":
    fs = 8000
    f1 = 3
    f2 = 3.5
    fft_size = 2 ** 17

    t, x1 = create_cos_wave(f1, fs)
    t, x2 = create_cos_wave(f2, fs)

    X1, w = cut_by_wind(t, x1)
    X2, w = cut_by_wind(t, x2)

    X1_dtl, w_dtl = cut_by_wind_fftsize(t, x1, fft_size)
    X2_dtl, w_dtl = cut_by_wind_fftsize(t, x2, fft_size)

    plt.subplot(2, 1, 1)
    plt.plot(w_dtl, X1_dtl, linestyle="dashed")
    plt.stem(w, X1)
    plt.xlim(0, 10)
    plt.xlabel("frequency[Hz]")
    plt.ylabel("Amplitude")
    plt.title("3Hz spectrum")

    plt.subplot(2, 1, 2)
    plt.plot(w_dtl, X2_dtl, linestyle="dashed")
    plt.stem(w, X2)
    plt.xlim(0, 10)
    plt.xlabel("frequency[Hz]")
    plt.ylabel("Amplitude")
    plt.title("3.5Hz spectrum")

    plt.tight_layout()
    plt.show()
