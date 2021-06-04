import numpy as np


def task3_2():
    # 定義
    fs = 44100
    r = 1.5
    f = 2
    L = 1/f
    t = np.arange(fs*L)/fs
    theta = 0.3

    # 観測信号
    x = r*np.cos(2*np.pi*t/L - theta)

    # sin cosの係数計算
    a = 2/fs/L*np.sum(np.dot(x, np.cos(2*np.pi*t/L)))
    b = 2/fs/L*np.sum(np.dot(x, np.sin(2*np.pi*t/L)))

    print('accu_r : {}, est_r : {}' .format(r, np.sqrt(a**2 + b**2)))
    print('accu_theta : {}, est_theta : {}' .format(theta, np.arctan2(b, a)))


if __name__ == '__main__':

    task3_2()
