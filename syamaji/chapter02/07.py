import numpy as np
import matplotlib.pyplot as plt

def task2_6():
  fs = 100
  t = np.arange(fs)/fs
  f = 1
  signal = np.sin(2*np.pi*f*t)

	#ノイズの作成
  noise = np.zeros((fs))
  pulse_n = 5
  for i in range(pulse_n):
    noise[np.random.randint((np.size(noise)))] = 2*np.round(np.random.rand())-1

  snr = 6
  #snr=6となるnoiseの生成
  noise = noise/np.sqrt(np.sum(noise**2))
  noise = noise*np.sqrt(np.sum(signal**2))
  noise = noise*10**(-snr/20)

	#mixture
  x = signal+noise

	#estimation by median filter
  y = np.zeros(len(x), dtype=float)
  M = 5
	#端部分の処理が甘い
  for i in range(len(y)):
  #for i in [i for i in range(M, len(y_moving_average)-M+1)]: 河村ver
    y[i] = np.median(x[i-M:i+M])

  #plot
  plt.subplot(3, 1, 1)
  plt.title('dry_signal')
  plt.plot(t, signal)
  plt.subplot(3, 1, 2)
  plt.title('x')
  plt.plot(t, x)
  plt.subplot(3, 1, 3)
  plt.title('y')
  plt.plot(t, y)
  plt.show()


if __name__ == "__main__":
	task2_6()