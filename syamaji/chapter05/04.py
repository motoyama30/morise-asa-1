import numpy as np
from func import MyHanning, MyHamming, MyBlackman


def task5_4():
    # 定義
    fs = 44100
    t = np.arange(fs) / fs
    f = 1000
    x = np.sin(2 * np.pi * f * t)
    fft_size = 65536
    w = np.arange(fft_size/2)*fs / fft_size

    X_han = np.fft.fft(x*MyHanning(x.shape[0]), fft_size)
    X_han = np.abs(X_han[:fft_size//2])
    spectral_centrois_han = np.sum(w*X_han)/np.sum(X_han)

    X_ham = np.fft.fft(x*MyHamming(x.shape[0]), fft_size)
    X_ham = np.abs(X_ham[:fft_size//2])
    spectral_centrois_ham = np.sum(w*X_ham)/np.sum(X_ham)

    X_bla = np.fft.fft(x*MyBlackman(x.shape[0]), fft_size)
    X_bla = np.abs(X_bla[:fft_size//2])
    spectral_centrois_bla = np.sum(w*X_bla)/np.sum(X_bla)

    print('Hanning window error:{}'.format(f - spectral_centrois_han))
    print('Hamming window error:{}'.format(f - spectral_centrois_ham))
    print('Blackman window error:{}'.format(f - spectral_centrois_bla))


if __name__ == "__main__":
    task5_4()
