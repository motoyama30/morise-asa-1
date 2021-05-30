# 高速フーリエ変換によるスペクトル解析
import numpy as np

np.random.seed(0)  # シード値


def create_random_signal(N):
    x = np.random.randn(N, 1)
    t = np.arange(N).reshape((N, 1))

    return t, x


def dft(N, t, x):
    c = np.zeros((N, 1), dtype="complex128")  # ゼロ埋めを行う(複素数範囲での配列の作成が必要)
    t = np.arange(N).reshape((N, 1))  # (N,1)の縦ベクトル

    # dftでの値の計算
    for i in range(N):
        c[i] = np.sum(x * np.exp(-1j * 2 * np.pi * i * t / N))

    return c


# FFT関数での値の計算(転置したとき)
def fft_t(x):
    x = x.T  # np.fft.fftの引数は、(1,8)
    X = np.fft.fft(x)

    return X.T


if __name__ == "__main__":
    N = 8  # 信号長
    t, x = create_random_signal(N)

    c = dft(N, t, x)
    X = np.fft.fft(x, axis=0)  # 軸の指定を行う
    X2 = fft_t(x)

    print(c)
    print(X)
    # 値が近いかを調べる（誤差を含める）
    print(np.isclose(c, X))
