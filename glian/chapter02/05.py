import numpy as np
import matplotlib.pyplot as plt

def main():
    fs = 100
    t = np.arange(fs) / fs
    f = 1

    signal = np.sin(2 * np.pi * f * t)
    noise = np.random.randn(fs)

    snr = 6
    # snr=6となるnoiseの生成
    noise = noise / np.sqrt(np.sum(noise ** 2)) #ノイズ正規化
    noise = noise * np.sqrt(np.sum(signal ** 2))
    noise = noise * 10 ** (-snr / 20)

    # 出力snr
    out_snr = 10 * np.log10(np.sum(signal ** 2) / np.sum(noise ** 2))
    print('input_snr : {}'.format(snr))
    print('output_snr : {}'.format(out_snr))

    # 混合
    x = signal + noise

    plt.subplot(2, 1, 1)
    plt.title('signal')
    plt.plot(t, signal)
    plt.subplot(2, 1, 2)
    plt.title('x')
    plt.plot(t, x)
    plt.show()

if __name__ == "__main__":
    main()