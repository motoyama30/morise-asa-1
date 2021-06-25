import numpy as np
import matplotlib.pyplot as plt


def create_chirp_signal(f1, f2, fs, T):
    """
    f1からf2までT秒かけて変化させる信号
    Args:
        f1 : 始まりの周波数 (int)
        f2 : 終わりの周波数 (int)
        fs : サンプリング周波数 (int)
        T  : 変化させる秒数 (int)

    Return
        t : サンプル点
        x : 生成したチャープ信号
    """
    t = np.arange(fs * T) / fs
    k = (f2 - f1) / T
    x = np.sin(2 * np.pi * (f1 * t + (k / 2) * t ** 2))
    return t, x


if __name__ == "__main__":
    fs = 8000
    T = 1
    f1 = 100
    f2 = 2000
    fft_size = 8000
    t, x = create_chirp_signal(f1, f2, fs, T)

    w = np.arange(fft_size) * fs / fft_size
    plt.plot(w, 20 * np.log10(np.abs(np.fft.fft(x, fft_size))))
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative power (dB)")
    plt.xlim(0, 3000)
    plt.ylim(-10, 50)
    plt.grid()
    plt.show()
