# ckを導出する
import numpy as np


def create_two_sounds(fs, f1, r1, theta1, f2, r2, theta2):
    # 重ね合わせの信号xを生成
    t = np.arange(fs).reshape((fs, 1))/fs  # (1,fs)の縦ベクトル
    x = r1*np.cos(2*np.pi*f1*t-theta1) + r2*np.cos(2*np.pi*f2*t-theta2)
    return t, x

# ckを導出する


def estimate_ck(fs, t, x, k, message=None):
    c = np.sum(x*np.exp(-1j*2*np.pi*k*t))/fs

    # 振幅と位相を計算する
    amplitude = np.abs(c)  # 絶対値を取得
    phase = np.angle(np.conj(c))  # np.conj()で複素共役を取得
    phase_raku = np.angle(c)  # 負号が含まれる形ならnp.conjを省略できる

    # 結果の表示
    print(f'amplitude from ck {message} : {amplitude}')  # 振幅なのでr1の半分の値が出てくる
    print(f'phase from ck {message} : {phase}')  # 位相
    print(f'phase from ck {message} : {phase_raku}')


if __name__ == '__main__':
    fs = 44100
    f1 = 1
    r1 = 1.5
    theta1 = 0.3
    f2 = 3
    r2 = 0.2
    theta2 = -1.1
    k1 = 1
    k3 = 3
    t, x = create_two_sounds(fs, f1, r1, theta1, f2, r2, theta2)
    estimate_ck(fs, t, x, k1, message='(k=1)')
    estimate_ck(fs, t, x, k3, message='(k=3)')
