# 0Hzとナイキスト周波数の振幅の検証
import numpy as np


def create_sound(fs, f, r, theta):
    t = np.arange(fs).reshape((fs, 1))/fs  # (1,fs)の縦ベクトル
    x = r*np.cos(2*np.pi*t*f-theta)
    return t, x


def estimate_amplitude(fs, f, t, x, message=None):

    c = np.sum(x*np.exp(-1j*2*np.pi*f*t))/fs
    amplitude = np.abs(c)

    return amplitude


if __name__ == '__main__':
    fs = 8
    theta = 0
    r = 0.5
    for f in range(9):  # fを0から8まで
        # 0,4,8の時に振幅が0.5になる
        t, x = create_sound(fs, f, r, theta)
        amplitude = estimate_amplitude(fs, f, t, x)

        print(f'amplitude (f = {f}Hz): {amplitude}')
