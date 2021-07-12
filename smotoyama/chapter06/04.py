import numpy as np
import matplotlib.pyplot as plt

fs = 44100
fft_size = 65536
fc = 100
w = np.arange(fft_size) / fft_size * fs
fc_index = np.round(fft_size * fc / fs) + 1
amp_spec = np.ones(fft_size // 2 + 1)
amp_spec[int(fc_index) :] = 0
fft_size2 = 65536 * 16
w2 = np.arange(fft_size2) / fft_size2 * fs


spec = np.block([amp_spec, amp_spec[-2:0:-1]])
impulse_response = np.fft.fftshift(np.real(np.fft.ifft(spec)))

plt.plot(w, np.abs(np.fft.fft(impulse_response, fft_size)), marker="o", ls="N = 2^16")
plt.plot(w2, np.abs(np.fft.fft(impulse_response, fft_size2)), label="N = 2^20")
plt.xlim(95, 105)
plt.ylim(0, 1.2)
plt.xlabel("Freqency(Hz)")
plt.ylabel("Amplitude")
plt.show()
