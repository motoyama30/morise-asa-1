import numpy as np


def task3_4():
    # 定義
    fs = 44100
    t = np.arange(fs - 1)/fs
    # 各周期，振幅，位相
    n1 = 1
    r1 = 1.5
    theta1 = 0.3
    n2 = 3
    r2 = 0.3
    theta2 = 1.1

    # 観測信号
    x = r1*np.cos(2*np.pi*n1*t - theta1) + r2*np.cos(2*np.pi*n2*t - theta2)

    # f=n1=1 の成分のみ抽出
    a = 2/fs*np.sum(np.dot(x, np.cos(2*np.pi*t)))
    b = 2/fs*np.sum(np.dot(x, np.sin(2*np.pi*t)))

    print('accu_r : {}, est_r : {}' .format(r1, np.sqrt(a**2 + b**2)))
    print('accu_theta : {}, est_theta : {}' .format(theta1, np.arctan2(b, a)))


if __name__ == '__main__':

    task3_4()
