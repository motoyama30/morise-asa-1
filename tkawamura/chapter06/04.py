import matplotlib.pyplot as plt
import numpy as np

fs = 44100
fft_size = 65536
fc = 100

w = np.arange(fft_size) / fft_size * fs
fc_index = int(np.round(fft_size * fc / fs)) + 1
amp_spec = np.ones(fft_size // 2 + 1)
amp_spec[fc_index:] = 0
spec = np.hstack((amp_spec, amp_spec[-2:0:-1]))
impulse_response = np.fft.fftshift(np.real(np.fft.ifft(spec)))

fft_size2 = 65536 * 16
w2 = np.arange(fft_size2) / fft_size2 * fs

plt.plot(w, np.abs(np.fft.fft(impulse_response)), "ko")
plt.plot(w2, np.abs(np.fft.fft(impulse_response, fft_size2)), "k")

plt.xlim(95, 105)
# plt.ylim(0, 1.2)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")

plt.grid()
plt.show()
