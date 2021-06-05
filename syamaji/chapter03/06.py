import numpy as np


def task3_6(fs):
    # 定義
    r = 0.5
    t = np.arange(fs)/fs

    for f in range(fs):
        x = r*np.cos(2*np.pi*f*t)
        c = np.sum(x * np.exp(-1j*2*np.pi*f*t))/fs
        print('fs : {}, f : {}, abs_c : {}' .format(fs, f, abs(c)))


if __name__ == '__main__':

    task3_6(8)
    task3_6(7)
