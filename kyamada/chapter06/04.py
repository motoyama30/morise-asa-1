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
    impluse_response = np.fft.fftshift(np.real(np.fft.ifft(spec)))

    return spec, impluse_response


if __name__ == "__main__":
    fs = 44100
    fft_size = 65536
    fc = 100  # カットオフ周波数
    fft_size2 = 65536 * 16

    w, amp_spec = create_amp_spec(fs, fft_size, fc)
    spec, impluse_response = shift_spec(amp_spec)
    w2 = np.arange(0, fft_size2) / fft_size2 * fs

    # プロットを行う
    plt.plot(w, np.abs(np.fft.fft(impluse_response)), "ko")
    plt.plot(w2, np.abs(np.fft.fft(impluse_response, fft_size2)))
    plt.xlim(95, 105)
    plt.ylim(0, 1.2)
    plt.grid()
    plt.xlabel("frequency [Hz]")
    plt.ylabel("amplitude")
    plt.show()
