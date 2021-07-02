import numpy as np
import matplotlib.pyplot as plt


def spectral_analysis_by_difference_equation(N):
    """
    Args:
        N:サンプル数
    Returns:
        k: spec1の大きさの配列
        spec1: 振幅スペクトル

    """
    k = np.arange(N)
    spec1 = np.abs(1 / (1 - 0.5 * np.exp(-1j * 2 * np.pi * k / N)))
    return k, spec1


def spectral_analysis_by_Fourier(N):
    """
    Args:
        N:サンプル数
    Returns:
        spec2: 振幅スペクトル
    """
    h = np.zeros(N)
    h[0] = 1
    for n in range(1, N):
        h[n] = 0.5 * h[n - 1]
    spec2 = np.abs(np.fft.fft(h))
    return spec2


if __name__ == "__main__":
    N = 128
    k, spec1 = spectral_analysis_by_difference_equation(N)
    spec2 = spectral_analysis_by_Fourier(N)

    plt.subplot(2, 1, 1)
    plt.plot(k, spec1)
    plt.xlim(0, N - 1)
    plt.xlabel("Discrete frequency")
    plt.ylabel("Amplitude")
    plt.title("spec1")
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(k, spec2)
    plt.xlim(0, N - 1)
    plt.xlabel("Discrete frequency")
    plt.ylabel("Amplitude")
    plt.title("spec2")
    plt.grid()

    plt.tight_layout()
    plt.show()
