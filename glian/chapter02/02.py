import numpy as np
import matplotlib.pyplot as plt


def main():
    n = np.arange(20)
    w = 0.1 * 2 * np.pi
    x1 = np.sin(w * n)
    x2 = np.sin((w + 2 * np.pi) * n)
    # sin(ωn)のプロット
    plt.subplot(2, 1, 1)
    plt.plot(n, x1)
    plt.title("sin(ωn)")  # タイトルの設定
    plt.xlabel("Time [sample]")  # 軸ラベルの設定
    plt.ylabel("Amplitude")  # 軸ラベルの設定
    plt.ylim(-1, 1)  # 軸の表示範囲を設定
    plt.grid()  # グリッドを表示

    # sin( (ω+2π) n)のプロット
    plt.subplot(2, 1, 2)
    plt.plot(n, x2)
    plt.title("sin( (ω+2π) n)")  # タイトルの設定
    plt.xlabel("Time [sample]")  # 軸ラベルの設定
    plt.ylabel("Amplitude")  # 軸ラベルの設定
    plt.ylim(-1, 1)  # 軸の表示範囲を設定
    plt.grid()  # グリッドを表示
    plt.tight_layout() #被らないように表示
    plt.show()

    plt.subplot(2, 1, 1)
    plt.plot(n, x1 - x2)
    plt.title("error with no range")  # タイトルの設定
    plt.xlabel("Time [sample]")  # 軸ラベルの設定
    plt.ylabel("Amplitude")  # 軸ラベルの設定
    plt.subplot(2, 1, 2)
    plt.plot(n, x1 - x2)
    plt.title("error with range (-1,1)")  # タイトルの設定
    plt.xlabel("Time [sample]")  # 軸ラベルの設定
    plt.ylabel("Amplitude")  # 軸ラベルの設定
    plt.ylim(-1, 1)  # 軸の表示範囲を設定

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()