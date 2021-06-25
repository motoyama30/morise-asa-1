import numpy as np

np.random.seed(0)  # シード値


def estimate_avarage_time_from_input_signal(x, fs):
    t = np.arange(len(x)) / fs
    t_c1 = np.sum(t * x ** 2) / fs
    return t_c1


def estimate_avarage_time_from_spectrum(x, fs):
    t = np.arange(len(x)) / fs

    fft_size = 2 ** np.ceil(np.log2(len(x)))
    X = np.fft.fft(x, int(fft_size))
    Xd = np.fft.fft(-1j * t * x, int(fft_size))
    tau_d = (np.real(Xd) * np.imag(X) - np.real(X) * np.imag(Xd)) / abs(X) ** 2
    t_c2 = np.sum(tau_d * abs(X) ** 2) / fs / fft_size
    return t_c2


if __name__ == "__main__":
    fs = 44100
    N = 22050
    x = np.random.randn(N)
    energy = np.sum(x ** 2) / fs
    x = x / np.sqrt(energy)
    t_c1 = estimate_avarage_time_from_input_signal(x, fs)
    t_c2 = estimate_avarage_time_from_spectrum(x, fs)
    print(f"{t_c1}")
    print(f"{t_c2}")
