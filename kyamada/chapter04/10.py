import numpy as np


def create_sound(fs, f):
    t = np.arange(fs) / fs
    x = np.sin(2 * np.pi * f * t)
    return t, x


def estimate_spectral_centroid(t, x, fft_size):
    X = np.fft.fft(x, fft_size)
    X = abs(X[0 : int(fft_size / 2 - 1)])

    w = np.arange(int(fft_size / 2 - 1)) * fs / fft_size
    spectral_centroid = np.sum(w * X) / np.sum(X)
    print(f"spectral_centroid [Hz]: {spectral_centroid}")


if __name__ == "__main__":
    fs = 44100
    f = 1000
    fft_size = 65536

    t, x = create_sound(fs, f)
    estimate_spectral_centroid(t, x, fft_size)
