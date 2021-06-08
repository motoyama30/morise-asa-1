import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import math


def task4_3():
    # 定義
    fs = 44100
    t = np.arange(fs) / fs
    f1 = 10
    f2 = 100
    r1 = 1
    r2 = 2
    x1 = r1 * np.sin(2 * np.pi * f1 * t)
    x2 = r2 * np.sin(2 * np.pi * f2 * t)
    x = x1 + x2
    X = np.fft.fft(x)

    print("{}".format(np.sum(x1 ** 2)))
    print("{}".format(np.sum(x2 ** 2)))
    print("{}".format(np.sum(x ** 2)))

4   p1 = 20 * np.log10(np.sum(np.abs(X[:19])))
    p2 = 20 * np.log10(np.sum(np.abs(X[90:109])))
    print("p1:{}".format(p1))
    print("p2:{}".format(p2))


if __name__ == "__main__":

    task4_3()
