import numpy as np
import matplotlib.pyplot as plt


def create_amp_spec(fs, fft_size, fc):
    """
    カットオフ周波数より高い周波数の時は振幅0,低い時は1の信号

    Args:
        fs: サンプリング周波数
        fft_size: FFT長
        fc : カットオフ周波数
    Returns:
        w: amp_specの軸設定用の信号
        amp_spec: カットオフ後の信号
    """
    w = np.arange(0, fft_size) / fft_size * fs
    fc_index = int(np.round(fft_size * fc / fs)) + 1
    amp_spec = np.ones(int(fft_size // 2 + 1))
    amp_spec[fc_index:-1] = 0
    return w, amp_spec


def shift_spec(amp_spec):
    # 繰り返し成分を生成する （スライスメモ:[開始位置:終了位置:間隔]）
    spec = np.concatenate([amp_spec, amp_spec[-2:0:-1]])
    impulse_response = np.fft.fftshift(np.real(np.fft.ifft(spec)))

    return spec, impulse_response


def my_blackman(N):
    n = np.arange(N)
    win = (
        0.42
        - 0.5 * np.cos(2 * np.pi * n / (N + 1))
        + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    )
    return win


if __name__ == "__main__":
    fs = 44100
    fft_size = 65536
    fc = 100  # カットオフ周波数
    fft_size2 = 65536 * 16
    half_N = 32767

    w, amp_spec = create_amp_spec(fs, fft_size, fc)
    spec, impulse_response = shift_spec(amp_spec)
    w2 = np.arange(0, fft_size2) / fft_size2 * fs

    # 補助のプロットを追加
    window_index = np.arange(fft_size // 2 - half_N, fft_size // 2 + half_N + 1)
    h = impulse_response[window_index] * my_blackman(half_N * 2 + 1)

    # プロットを行う
    plt.plot(w, np.abs(np.fft.fft(impulse_response)), "ko")
    plt.plot(w2, np.abs(np.fft.fft(impulse_response, fft_size2)), "k--")
    plt.plot(w2, np.abs(np.fft.fft(h, fft_size2)))
    plt.xlim(95, 105)
    plt.ylim(0, 1.2)
    plt.grid()
    plt.xlabel("frequency [Hz]")
    plt.ylabel("amplitude")
    plt.show()
