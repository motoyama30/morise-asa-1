import matplotlib.pyplot as plt
import numpy as np


def MyBlackman(N):
    n = np.arange(N)
    win = (
        0.42
        - 0.5 * np.cos(2 * np.pi * n / (N - 1))
        + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    )

    return win


def MinimumPhase(x):
    x_len_half = np.size(x) // 2 - 1
    X = np.real(np.fft.ifft(np.log(np.abs(np.fft.fft(x)))))
    w = np.hstack((1, 2 * np.ones(x_len_half), 1, np.zeros(x_len_half)))
    y = np.real(np.fft.ifft(np.exp(np.fft.fft(w * X))))

    return y


fs = 44100
fft_size = 65536
fc = 100

w = np.arange(fft_size) / fft_size * fs
fc_index = int(np.round(fft_size * fc / fs)) + 1
amp_spec = np.ones(fft_size // 2 + 1)
amp_spec[fc_index:] = 0.01
spec = np.hstack((amp_spec, amp_spec[-2:0:-1]))
impulse_response = np.fft.fftshift(np.real(np.fft.ifft(spec)))
impulse_response[0] = 0
impulse_response[1 : fft_size + 1] = impulse_response[1 : fft_size + 1] * MyBlackman(
    fft_size - 1
)
minimum_phase_response = MinimumPhase(impulse_response)

fft_size2 = 65536 * 16
w2 = np.arange(fft_size2) / fft_size2 * fs

plt.plot(w2, np.abs(np.fft.fft(impulse_response, fft_size2)), "k")
plt.plot(w2, np.abs(np.fft.fft(minimum_phase_response, fft_size2)), "k--")

plt.xlim(95, 105)
# plt.ylim(0, 1.2)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")

plt.grid()
plt.show()
