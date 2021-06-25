import numpy as np
import matplotlib.pyplot as plt


def create_sound(fs, f):
    t = np.arange(fs * 2) / fs
    x = np.sin(2 * np.pi * f * t)
    return t, x


def analyze_spectrum(fs, x):
    X = np.fft.fft(x)
    w = np.arange(len(x)) * fs / len(x)
    plt.plot(w, abs(X))
    plt.xlim(0, 50)  # x軸の範囲を指定する
    plt.xlabel("frequency [Hz]")
    plt.ylabel("amplitude")
    plt.show()


if __name__ == "__main__":
    fs = 44100
    f = 5
    t, x = create_sound(fs, f)
    analyze_spectrum(fs, x)
