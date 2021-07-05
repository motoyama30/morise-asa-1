import numpy as np
import matplotlib.pyplot as plt


def task6_3():
  # 定義
  N = 128
  k = np.arange(N)
  spec1 = abs(1 / (1 - 0.5 * np.exp(-1j * 2 * np.pi * k / N)))
  h = np.zeros(N)
  h[0] = 1
  for n in range(1, N):
      h[n] = 0.5 * h[n - 1]
  spec2 = abs(np.fft.fft(h))

  # plot
  plt.subplot(2, 1, 1)
  plt.plot(k, spec1)
  plt.title("Spec1")
  plt.xlim(0, N - 1)

  plt.subplot(2, 1, 2)
  plt.plot(k, spec2)
  plt.title("Spec2")
  plt.xlim(0, N - 1)

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
    task6_3()
