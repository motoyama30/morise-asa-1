
import numpy as np


def task2_1():
    # 定義
    fs = 44100
    t = np.arange(fs/2-1)/fs
    x = np.sin(2*np.pi*t)

    # 区分求積法
    S = sum(x)/fs
    # 表示
    print('S : {}' .format(S))


if __name__ == '__main__':

    task2_1()
