import numpy as np


def task3_1():
    # 定義
    fs = 44100
    t = np.arange(fs)/fs
    r = 1.5
    theta = 0.3

    # 観測信号
    x = r*np.cos(2*np.pi*t - theta)
    # sin cosの係数計算
    a = 2/fs*np.sum(x * np.cos(2*np.pi*t))
    b = 2/fs*np.sum(x * np.sin(2*np.pi*t))

    print('accu_r : {}, est_r : {}' .format(r, np.sqrt(a**2 + b**2)))
    print('accu_theta : {}, est_theta : {}' .format(theta, np.arctan2(b, a)))


if __name__ == '__main__':

    task3_1()
