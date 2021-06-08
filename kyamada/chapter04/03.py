import numpy as np
import matplotlib.pyplot as plt


def create_sound(fs, f):
    t = np.arange(fs * 2) / fs
    x = np.sin(2 * np.pi * f * t)
    return t, x


def zero_padding(x):
    print()
    fft_size = 2 ** (np.ceil(np.log2(len(x))))
    return int(fft_size)


def analyze_spectrum(fs, x, fft_size=None):
    if fft_size == None:
        fft_size = len(x)
    X1 = np.fft.fft(x)
    X2 = np.fft.fft(x, fft_size)
    w = np.arange(fft_size) * fs / fft_size
    plt.plot(w, abs(X2))
    plt.xlim(0, 50)  # x軸の範囲を指定する
    plt.xlabel("frequency [Hz]")
    plt.ylabel("amplitude")
    plt.show()

    return X1, X2


def check_parsevals_theorem(x, X1, X2):
    x_amp = np.sum(x ** 2)
    non_zero_fft_power = np.sum(abs(X1) ** 2) / len(X1)
    zero_fft_power = np.sum(abs(X2) ** 2) / len(X2)
    print(f"(x's amp) ^2 : {x_amp}")
    print(f"non zero padding FFT's power : {non_zero_fft_power}")
    print(f"zero padding FFT's power : {zero_fft_power}")


if __name__ == "__main__":
    fs = 44100
    f = 5
    t, x = create_sound(fs, f)
    fft_size = zero_padding(x)
    X1, X2 = analyze_spectrum(fs, x, fft_size)
    check_parsevals_theorem(x, X1, X2)
