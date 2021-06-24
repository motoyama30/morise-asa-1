import numpy as np
from func import MyHanning, MyHamming, MyBlackman
import matplotlib.pyplot as plt
import pylab as pl


def task5_8(stft_time, win_func, output_path=None):

    #################################
    # stft_time   ：STFT長 [ms]
    # win_func    ：窓関数（関数）
    # output_path ：スペクトログラムの保存先(default=None)
    #################################

    # 定義
    fs = 8000
    T = 1
    f1 = 100
    f2 = 2000
    k = (f2-f1)/T
    t = np.arange(fs*T) / fs
    x = np.sin(2*np.pi*(f1*t+(k/2)*t**2))

    win_len = np.round(fs*stft_time)
    win = win_func(win_len)
    fft_size = int(2**np.ceil(np.log2(win_len)))
    frame_shift = np.round(fs*(stft_time/2))
    number_of_frames = int(np.ceil((x.shape[0])/frame_shift))
    X = np.zeros([int(fft_size//2), number_of_frames])
    bace_index = np.arange(np.ceil(-win_len//2), np.ceil(win_len//2), dtype=int)


    for i in range(number_of_frames):
        center = np.round(i*frame_shift)
        safe_index = np.zeros_like(bace_index)
        tmp = np.zeros_like(bace_index)
        
        bace_index = bace_index +int(center)
        a = np.minimum(bace_index , x.shape[0])
        safe_index = np.maximum(np.minimum(bace_index , x.shape[0]), 1)
        tmp = x[safe_index] * win 
        tmpX = 20*np.log10(np.abs(np.fft.fft(tmp, fft_size)))
        X[:, i] = tmpX[:fft_size//2]

    I, J = X.shape
    x, y = pl.meshgrid(pl.arange(J+1), pl.arange(I+1))

    plt.figure()
    pl.pcolormesh(x, y, X)
    plt.colorbar()

    if output_path is None:
        pl.show()
    else:
        pl.savefig(output_path)


if __name__ == "__main__":
    # Fig.の保存Path
    output_path = None

    # for STFT長 [ms]
    for idx, stft_time in enumerate([0.02, 0.01]):
        # for 窓関数
        for win_func in [MyHanning, MyHamming, MyBlackman]:
            # 窓願数とSTFT長で命名
            output_path = './chapter05/fig/{}_{}ms'.format(str(win_func.__name__), int(stft_time * 1000))
            task5_8(stft_time, win_func, output_path)