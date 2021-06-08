import numpy as np

np.random.seed(0)  # シード値


def estimate_duration_from_input_signal(x, fs):
    t = np.arange(len(x)) / fs
    t_c1 = np.sum(t * x ** 2) / fs
    sigma_t1 = np.sum((t - t_c1) ** 2 * x ** 2) / fs
    return sigma_t1


def estimate_duration_from_spectrum(x, fs):
    fft_size = 2 ** np.ceil(np.log2(len(x)))
    t = np.arange(len(x)) / fs
    t_c = sum(t * x ** 2) / fs
    X = np.fft.fft(x, int(fft_size))
    Xd = np.fft.fft(-1j * t * x, int(fft_size))
    tau_d = (np.real(Xd) * np.imag(X) - np.real(X) * np.imag(Xd)) / abs(X) ** 2
    d1 = ((np.real(X) * np.real(Xd) + np.imag(X) * np.imag(Xd)) / abs(X)) ** 2
    d2 = (-tau_d + t_c) ** 2 * abs(X) ** 2
    sigma_t2 = (np.sum(d1) + np.sum(d2)) / fft_size / fs

    return sigma_t2


if __name__ == "__main__":
    fs = 44100
    N = 22050
    x = np.random.randn(N)
    energy = np.sum(x ** 2) / fs
    x = x / np.sqrt(energy)
    sigma_t1 = estimate_duration_from_input_signal(x, fs)
    sigma_t2 = estimate_duration_from_spectrum(x, fs)
    print(f"{sigma_t1}")
    print(f"{sigma_t2}")
