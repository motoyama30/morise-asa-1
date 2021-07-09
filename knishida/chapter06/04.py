import numpy as np
import matplotlib.pyplot as plt


# declare
fs = 44100
fft_size = 65536
fc = 100
w = np.arange(0, fft_size) / fft_size * fs

# calc
fc_index = np.round(fft_size * fc / fs) + 1
amp_spec = np.ones(int(fft_size // 2) + 1)
amp_spec[int(fc_index) :] = 0

spec = np.block([amp_spec, amp_spec[-2:0:-1]])


impulse_response = np.fft.fftshift(np.real(np.fft.ifft(spec)))

fft_size2 = 65536 * 16
w2 = np.arange(0, fft_size2) / fft_size2 * fs

plt.plot(w, np.abs(np.fft.fft(impulse_response, fft_size)), marker="o", ls="None")
plt.plot(w2, np.abs(np.fft.fft(impulse_response, fft_size2)))
plt.xlim(95, 105)
plt.ylim(0, 1.2)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.show()
