import numpy as np


def my_hanning(N):
    n = np.arange(N)
    win = (1 - np.cos(2 * np.pi * n / (N + 1))) / 2
    return win


def my_hamming(N):
    n = np.arange(N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N + 1))
    return win


def my_blackman(N):
    n = np.arange(N)
    win = (
        0.42
        - 0.5 * np.cos(2 * np.pi * n / (N + 1))
        + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    )
    return win


def create_sin_wave(f, fs):
    t = np.arange(fs) / fs
    x = np.sin(2 * np.pi * f * t)
    return t, x


def estimate_spectre_centroid(w, x, wind, fft_size):
    X = np.fft.fft(x * wind, fft_size)
    X = np.abs(X[0 : int(fft_size / 2) + 1])
    spectral_centroid = np.sum(w * X) / np.sum(X)

    return X, spectral_centroid


if __name__ == "__main__":
    fs = 44100
    f = 1000
    fft_size = 65536

    t, x = create_sin_wave(f, fs)

    w = np.arange(int(fft_size / 2 + 1)) * fs / fft_size  # 配列サイズの確認する

    X_han, spectral_centroid_han = estimate_spectre_centroid(
        w, x, my_hanning(len(x)), fft_size
    )
    X_ham, spectral_centroid_ham = estimate_spectre_centroid(
        w, x, my_hamming(len(x)), fft_size
    )
    X_bla, spectral_centroid_bla = estimate_spectre_centroid(
        w, x, my_blackman(len(x)), fft_size
    )
    print(f"Hanning window: {spectral_centroid_han}")
    print(f"Hanning window: {spectral_centroid_ham}")
    print(f"Hanning window: {spectral_centroid_bla}")
