import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 44100
fft_size = 65536
fc = 100
fft_size2 = 65536 * 16

w = np.arange(0, fft_size) / fft_size * fs
fc_index = round(fft_size * fc / fs) + 1
amp_spec = np.ones(fft_size // 2 + 1)
amp_spec[fc_index:] = 0

spec = np.block([amp_spec, amp_spec[-2:0:-1]])
impulse_response = np.fft.fftshift(np.fft.ifft(spec).real)

w2 = np.arange(0, fft_size2) / fft_size2 * fs

plt.plot(
    w, abs(np.fft.fft(impulse_response)), color="k", marker="o", ls="None", mfc="None"
)
plt.plot(w2, abs(np.fft.fft(impulse_response, fft_size2)), color="k")
plt.xlim(95, 105)
plt.xlabel("frequency [Hz]")
plt.ylabel("amplitude")
plt.show()
