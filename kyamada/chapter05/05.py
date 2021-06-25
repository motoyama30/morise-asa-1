import numpy as np
import matplotlib.pyplot as plt


def clc_fftsift_rect(N, fft_size, fs):
    win_rect = np.ones(int(N))
    W_rect = np.fft.fftshift(np.abs(np.fft.fft(win_rect, fft_size)))
    W_rect = W_rect / np.max(W_rect)
    w = np.arange(fft_size) / fft_size * fs - fs / 2
    return w, W_rect


if __name__ == "__main__":
    fs = 44100
    fft_size = 65536

    N = np.round(fs * 0.02)  # 四捨五入を行う
    w, W_rect = clc_fftsift_rect(N, fft_size, fs)

    plt.plot(w, W_rect)
    plt.xlim(-400, 400)
    plt.ylim(0, 1)
    plt.xlabel("frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.show()
