import numpy as np
import matplotlib.pyplot as plt

def main():
  fs = 100
  t = np.arange(fs)/fs
  f = 1
  #信号とノイズの生成
  signal = np.sin(2*np.pi*f*t)
  noise = np.random.randn(fs)
  snr = 6
  noise = noise/np.sqrt(np.sum(noise**2))
  noise = noise*np.sqrt(np.sum(signal**2))
  noise = noise*10**(-snr/20)

  x = signal+noise

#移動平均フィルタ
  y = np.zeros(len(x), dtype=float)
  M = 5

  for i in range(M, len(y)): # xは0から
    y[i] = np.mean(x[i-M:i+M])

  #plot
  plt.subplot(3, 1, 1)
  plt.title('signal')
  plt.plot(t, signal)
  plt.subplot(3, 1, 2)
  plt.title('signal+noise')
  plt.plot(t,x)
  plt.subplot(3, 1, 3)
  plt.title('moving mean_y')
  plt.plot(t,y)
  plt.tight_layout()
  plt.show()
  plt.close()


if __name__ == "__main__":
    main()