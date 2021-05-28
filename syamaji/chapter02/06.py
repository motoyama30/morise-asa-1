import numpy as np
import matplotlib.pyplot as plt

def task2_6():
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

	#mixture
  x = signal+noise

	#estimation by moving average filter
  y = np.zeros(len(x), dtype=float)
  M = 5
	#端部分の処理が甘い
  for i in range(len(y)):
  #for i in [i for i in range(M, len(y_moving_average)-M+1)]: 河村ver
    y[i] = np.mean(x[i-M:i+M])

  #plot
  plt.subplot(3, 1, 1)
  plt.title('dry_signal')
  plt.plot(t, signal)
  plt.subplot(3, 1, 2)
  plt.title('x')
  plt.plot(t,x)
  plt.subplot(3, 1, 3)
  plt.title('y')
  plt.plot(t,y)
  plt.show()


if __name__ == "__main__":
	task2_6()