import numpy as np
import matplotlib.pyplot as plt


def main():
    fs = 44100  # 標本化周波数 [Hz]
    len_t = 1   #信号長
    t = np.arange(fs*len_t) / fs  # 時間インデックス [秒]
    x = np.sin(2 * np.pi * t)  # 波形（正弦波)

    plt.plot(t, x)
    plt.show()
    plt.close()
    S = sum(x) / fs  # 区分求積法
    print("S =  {}".format(S))

if __name__ == "__main__":
    main()
