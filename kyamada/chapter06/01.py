import numpy as np
import sounddevice as sd


def create_white_noise(fs):
    """create_white_noise
    Args
        fs : サンプリング周波数
    Returns
        x: ホワイトノイズのNumpy配列
    """
    x = np.random.randn(fs)
    return x


def low_cut(x, fs):
    """low_cut
    Args
        x : 処理する信号
        fs : サンプリング周波数
    Returns
        y: ローカットした後の信号
    """
    y = np.zeros(fs)
    y[0] = 0.5 * x[0]
    for n in range(1, len(x)):
        y[n] = 0.5 * x[n] - 0.5 * x[n - 1]
    return y


if __name__ == "__main__":
    fs = 44100
    x = create_white_noise(fs)
    y = low_cut(x, fs)

    # 音声の再生
    print("xのノイズの再生")
    sd.play(x)
    sd.wait()
    print("yのノイズの再生")
    sd.play(y)
    sd.wait()
