# パワースペクトルの算出
import numpy as np
import matplotlib.pyplot as plt

# ハニング窓生成
def MyHanning(N):
    n = np.arange(N)
    win = (1 - np.cos(2 * np.pi * n / (N - 1))) / 2
    return win


# ハミング窓生成
def MyHamming(N):
    n = np.arange(N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return win


# ブラックマン窓生成
def MyBlackman(N):
    n = np.arange(N)
    win = (
        0.42
        - 0.5 * np.cos(2 * np.pi * n / (N - 1))
        + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    )
    return win


# 信号生成
fs = 44100
N = int(np.round(fs * 0.02))
fft_size = 65536

win_han = MyHanning(N)
W_han = np.abs(np.fft.fft(win_han, fft_size))
np.place(W_han, W_han == 0, 10 ** (-10))
W_han = 20 * np.log10(W_han)
W_han = np.fft.fftshift(W_han) - np.max(W_han)

win_ham = MyHamming(N)
W_ham = np.abs(np.fft.fft(win_ham, fft_size))
np.place(W_ham, W_ham == 0, 10 ** (-10))
W_ham = 20 * np.log10(W_ham)
W_ham = np.fft.fftshift(W_ham) - np.max(W_ham)

win_bla = MyBlackman(N)
W_bla = np.abs(np.fft.fft(win_bla, fft_size))
np.place(W_bla, W_bla == 0, 10 ** (-10))
W_bla = 20 * np.log10(W_bla)
W_bla = np.fft.fftshift(W_bla) - np.max(W_bla)

# グラフ描画
w = np.arange(fft_size) / fft_size * fs - fs / 2
plt.plot(w, W_han, label="Hanning window")
plt.plot(w, W_ham, "--", label="Hamming window")
plt.plot(w, W_bla, "-.", label="Blackman window")
plt.xlim(-400, 400)
plt.ylim(-80, 0)
plt.title("Power spectrum of 3 window functions")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Power [dB]")
plt.legend()
plt.show()
