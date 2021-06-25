import numpy as np
import matplotlib.pyplot as plt


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


def set_stft_param(win_len):
    fft_size = int(2 ** np.ceil(np.log2(win_len)))
    frame_shift = int(np.round(fs * 0.01))
    number_of_frames = int(np.ceil(len(x) / frame_shift))
    X = np.zeros((int(fft_size / 2), number_of_frames))
    base_index = np.arange(np.ceil(-win_len / 2), np.ceil(win_len / 2))
    return fft_size, frame_shift, number_of_frames, X, base_index


def time_frequency_analysis(
    x, fs, win_len, win, fft_size, frame_shift, number_of_frames, X, base_index
):

    for i in range(number_of_frames):
        center = int(np.round(i * frame_shift))  # 信号を切り出す中心時刻
        # safe_index は、0以下の時は、1になる
        safe_index = np.where(base_index <= 0, 1, base_index)
        safe_index = np.where(safe_index > len(x), len(x), safe_index + center)
        # tmp[j]にx[safe_index[j]]の値を代入する
        tmp = np.zeros(len(safe_index))

        for j in range(len(safe_index)):
            tmp[j] = x[int(safe_index[j])]
        tmp = tmp * win  # 切り出して窓関数をかける
        tmpX = 20 * np.log10(np.abs(np.fft.fft(tmp, fft_size)))  # fft
        X[:, i] = tmpX[0 : int(fft_size / 2)]

    return X


if __name__ == "__main__":
    fs = 8000
    T = 1
    f1 = 100
    f2 = 2000
    fft_size = 8000

    # create chirp signal
    t, x = create_chirp_signal(f1, f2, fs, T)

    # set params
    win_len = np.round(fs * 0.02)
    fft_size, frame_shift, number_of_frames, X, base_index = set_stft_param(win_len)
    # STFT
    win = my_hanning(win_len)
    X = time_frequency_analysis(
        x, fs, win_len, win, fft_size, frame_shift, number_of_frames, X, base_index
    )

    plt.imshow(
        X,
        cmap="gray",
        origin="lower",
        extent=(0, 1, 0, 4000),
        vmax=np.max(X),
        aspect="auto",
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.colorbar()
    plt.show()

