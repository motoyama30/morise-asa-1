# チャープ信号の時間周波数解析
import numpy as np
import matplotlib.pyplot as plt

# ハニング窓生成
def MyHanning(N):
    n = np.arange(N)
    win = (1 - np.cos(2 * np.pi * n / (N - 1))) / 2
    return win


# 時間信号定義
fs = 8000
T = 1
f1 = 100
f2 = 2000
k = (f2 - f1) / T
t = np.arange(fs * T) / fs
x = np.sin(2 * np.pi * (f1 * t + (k / 2) * t ** 2))

# パラメータ設定
win_len = int(np.round(fs * 0.02))
win = MyHanning(win_len)
fft_size = int(2 ** np.ceil(np.log2(win_len)))
frame_shift = int(np.round(fs * 0.01))
number_of_frames = int(np.ceil((np.size(x) / frame_shift)))
X = np.zeros([int(fft_size // 2), number_of_frames])
base_index = np.arange(int(np.ceil(-win_len // 2)), int(np.ceil(win_len // 2)))

# 時間周波数解析
for i in range(number_of_frames):
    center = int(np.round(i * frame_shift))
    safe_index = np.maximum(0, np.minimum(np.size(x) - 1, base_index + center))
    tmp = x[safe_index] * win
    tmpX = 20 * np.log10(np.abs(np.fft.fft(tmp, fft_size)))
    X[:, i] = tmpX[: fft_size // 2]

plt.imshow(
    X,
    cmap="gray",
    origin="lower",
    extent=(0, 1, 0, 4000),
    vmax=np.max(X),
    aspect="auto",
)
plt.title("Spectrogram of chirp signal")
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
plt.colorbar()
plt.show()
