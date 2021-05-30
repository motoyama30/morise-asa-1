import numpy as np
import matplotlib.pyplot as plt

def main():
  fs = 100
  t = np.arange(fs)/fs
  f = 1
  signal = np.sin(2*np.pi*f*t)
  noise = np.zeros((fs))
  pulse_n = 5
  for i in range(pulse_n):
    noise[np.random.randint((fs))] = 2*np.round(np.random.rand())-1

  snr = 6
  #snr=6となるnoiseの生成
  noise = noise/np.sqrt(np.sum(noise**2))
  noise = noise*np.sqrt(np.sum(signal**2))
  noise = noise*10**(-snr/20)

  x = signal+noise
#medianフィルタ
  y = np.zeros(len(x), dtype=float)
  M = 5
  for i in range(M, len(y)):
    y[i] = np.median(x[i-M:i+M])

  plt.subplot(3, 1, 1)
  plt.title('signal')
  plt.plot(t, signal)
  plt.subplot(3, 1, 2)
  plt.title('signal + noise')
  plt.plot(t, x)
  plt.subplot(3, 1, 3)
  plt.title('median_y')
  plt.plot(t, y)
  plt.tight_layout()
  plt.show()

if __name__ == "__main__":
	main()