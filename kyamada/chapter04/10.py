import numpy as np


def create_sound(fs, f):
    t = np.arange(fs) / fs
    x = np.sin(2 * np.pi * f * t)
    return t, x


def estimate_spectral_centroid(t, x, fft_size):
    X = np.fft.fft(x, fft_size)
    print(X.shape, int(fft_size / 2))  # (65536,) 32768
    X = abs(X[0 : int(fft_size / 2 + 1)])
    print(X.shape)  # 32769
    # print("X", X.shape)
    w = np.arange(int(fft_size / 2 + 1)) * fs / fft_size
    spectral_centroid = np.sum(w * X) / np.sum(X)
    print(f"spectral_centroid [Hz]: {spectral_centroid}")


def debug_check_array_size():
    print("Debug")
    a = np.arange(100)
    a1 = a[1:50]
    print(a1)  # 1から49まで
    print(a1.shape)  # 49
    # matlabで a(1:50)を行ったときサイズが50になる
    # >> a = (1:100)  % 1x100
    # >> a1 = a(1:50) % 1x50


if __name__ == "__main__":
    fs = 44100
    f = 1000
    fft_size = 65536

    t, x = create_sound(fs, f)
    estimate_spectral_centroid(t, x, fft_size)

    # デバック
    debug_check_array_size()
