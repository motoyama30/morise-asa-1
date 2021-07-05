import numpy as np
from scipy.io.wavfile import write


def task6_1():
    # 定義
    fs = 44100
    x = np.random.randn(fs)
    y = np.zeros(fs)
    y[0] = 0.5*x[0]
    for n in range(1, x.shape[0]):
        y[n] = 0.5*x[n] - 0.5*x[n-1]

    write('./syamaji/chapter06/out.wav', fs, x)


if __name__ == "__main__":
    task6_1()
