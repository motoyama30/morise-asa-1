import numpy as np


def create_sound(fs, f, r):
    t = np.arange(fs) / fs
    x = r * np.sin(2 * np.pi * f * t)
    return t, x


def check_error(X):
    p1 = 20 * np.log10(np.sum(abs(X[0:19])))
    p2 = 20 * np.log10(np.sum(abs(X[90:109])))
    print(f"power of near 10Hz[db]:{p1}")
    print(f"power of near 100Hz[db]:{p2}")
    return p1, p2


if __name__ == "__main__":
    fs = 44100
    f1 = 10
    f2 = 100
    r1 = 1
    r2 = 2

    t, x1 = create_sound(fs, f1, r1)
    t, x2 = create_sound(fs, f2, r2)
    x = x1 + x2
    X = np.fft.fft(x)
    print(f"(x1's amp) ^2: {np.sum(x1 ** 2)}")
    print(f"(x2's amp) ^2: {np.sum(x2 ** 2)}")
    print(f"(x's amp) ^2: {np.sum(x ** 2)}")
    check_error(X)
