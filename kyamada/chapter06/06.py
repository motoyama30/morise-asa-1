import numpy as np
import matplotlib.pyplot as plt


def create_amp_spec(fs, fft_size, fc):
    """
    カットオフ周波数より高い周波数の時は振幅0.01,低い時は1の信号

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
    amp_spec[fc_index:-1] = 0.01
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


def minimum_phase(x):
    x_len_half = np.size(x) // 2 - 1
    X = np.real(np.fft.ifft(np.log(np.abs(np.fft.fft(x)))))
    w = np.hstack((1, 2 * np.ones(x_len_half), 1, np.zeros(x_len_half)))
    y = np.real(np.fft.ifft(np.exp(np.fft.fft(w * X))))

    return y


if __name__ == "__main__":
    fs = 44100
    fft_size = 65536
    fc = 100  # カットオフ周波数
    fft_size2 = 65536 * 16

    w, amp_spec = create_amp_spec(fs, fft_size, fc)
    spec, impluse_response = shift_spec(amp_spec)
    w2 = np.arange(0, fft_size2) / fft_size2 * fs

    impulse_response = np.fft.fftshift(np.real(np.fft.ifft(spec)))
    impulse_response[0] = 0
    impulse_response[1 : fft_size + 1] = impulse_response[
        1 : fft_size + 1
    ] * my_blackman(fft_size - 1)
    minimum_phase_response = minimum_phase(impulse_response)

    # プロットを行う
    plt.plot(w2, np.abs(np.fft.fft(impulse_response, fft_size2)), "k")
    plt.plot(w2, np.abs(np.fft.fft(minimum_phase_response, fft_size2)), "k--")
    plt.xlim(95, 105)
    plt.ylim(0, 1.2)
    plt.grid()
    plt.xlabel("frequency [Hz]")
    plt.ylabel("amplitude")
    plt.show()
