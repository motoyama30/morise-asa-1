import numpy as np
import matplotlib.pyplot as plt


fs = 44100
t = np.arange(0, fs) / fs
x1 = np.zeros(fs)
x2 = np.zeros(fs)

x1[int(fs / 2 - 500) : int(fs / 2 + 500 + 1)] = 1
x2[int(fs / 4 - 1000) : int(fs / 4 + 1000 + 1)] = 1

# 出力結果の違いについての確認１
# x1[int(fs/2-500):int(fs/2+500)] = 1
# x2[int(fs/4-1000):int(fs/4+1000)] = 1
# 出力結果の違いについての確認２
# x1[int(fs/2-500+1):int(fs/2+500+1)] = 1
# x2[int(fs/4-1000+1):int(fs/4+1000+1)] = 1

# 結果のプロット
fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(t, x1)
ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Amplitude")
ax1.set_title("x1")

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(t, x2)
ax2.set_xlabel("Time [s]")
ax2.set_ylabel("Amplitude")
ax2.set_title("x2")

plt.tight_layout()
plt.show()


energy = sum(x1 ** 2) / fs
xx1 = x1 / np.sqrt(energy)

t_c = sum(t * xx1 ** 2) / fs
sigma_t = sum((t - t_c) ** 2 * xx1 ** 2) / fs

t_c1 = sum(t * xx1 ** 2) / fs
t_c2 = sum(t ** 2 * xx1 ** 2) / fs
sigma_t2 = t_c2 - t_c1 ** 2


# 結果の出力
print("energy centroid: {:.10f}".format(t_c))
print("duration       : {:.10f}".format(sigma_t))
print("duration       : {:.10f}".format(sigma_t2))
print(
    "duration       : {:.10f}".format(fs / sum(x1 ** 2) / 3 * (2 * (500.5 / fs) ** 3))
)
