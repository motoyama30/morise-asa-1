# パラメータ推定のプログラム
import numpy as np


def create_sound(fs, r, theta):
    # 振幅rと位相θをパラメータとした1Hzの正弦波の生成
    t = np.arange(fs).reshape((fs, 1)) / fs  # (1,fs)の縦ベクトル
    x = r * np.cos(2 * np.pi * t - theta)
    return t, x


def estimate_a_b(fs, t, x):
    # a,bの計算（式より）
    a = 2 / fs * np.sum(x * np.cos(2 * np.pi * t))  # mTの代わりに計算結果が同じtを使う
    b = 2 / fs * np.sum(x * np.sin(2 * np.pi * t))

    # 振幅と位相の取得
    amplitude = np.sqrt(a ** 2 + b ** 2)
    phase = np.arctan2(b, a)

    return amplitude, phase


if __name__ == "__main__":
    fs = 44100
    r = 1.5
    theta = 0.3
    t, x = create_sound(fs, r, theta)
    amplitude, phase = estimate_a_b(fs, t, x)

    print(f"amplitude : {amplitude}")
    print(f"phase : {phase}")
