import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize


def MyHanning(N):
    n = np.arange(N)
    win = (1 - np.cos(2 * np.pi * n / (N - 1))) / 2

    return win


def MyHamming(N):
    n = np.arange(N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))

    return win


def MyBlackman(N):
    n = np.arange(N)
    win = (
        0.42
        - 0.5 * np.cos(2 * np.pi * n / (N - 1))
        + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    )

    return win


fs = 8000
T = 1
f1 = 100
f2 = 2000
k = (f2 - f1) / T
t = np.arange(fs * T) / fs
x = np.sin(2 * np.pi * (f1 * t + (k / 2) * t ** 2))

idx = 1  # subplot 表示用
for win in [MyHanning, MyHamming, MyBlackman]:
    for win_len in [np.round(fs * 0.02), np.round(fs * 0.01)]:
        fft_size = int(2 ** np.ceil(np.log2(win_len)))
        frame_shift = int(np.round(fs * 0.01))
        number_of_frames = int(np.ceil((np.size(x) + 1) / frame_shift))
        X = np.zeros((int(fft_size / 2), number_of_frames))
        base_index = np.arange(int(np.ceil(-win_len / 2)), int(np.ceil(win_len / 2)))

        plt.subplot(3, 2, idx)
        for i in range(number_of_frames):
            center = int(np.round(i * frame_shift))
            safe_index = np.maximum(0, np.minimum(np.size(x) - 1, base_index + center))
            tmp = x[safe_index] * win(win_len)
            tmpX = 20 * np.log10(np.abs(np.fft.fft(tmp, fft_size)))
            X[:, i] = tmpX[: int(fft_size / 2)]

        idx = idx + 1

        librosa.display.specshow(
            X,
            sr=fs,
            hop_length=frame_shift,
            cmap="gray",
        )

        plt.xlabel("Time [s]")
        plt.ylabel("Frequency [Hz]")
        plt.colorbar()
        plt.tight_layout()

plt.show()
