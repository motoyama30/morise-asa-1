
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import math

def task2_5():
  #定義
  fs = 100
  t = np.arange(fs)/fs
  f = 1

  #信号とノイズの生成
  signal = np.sin(2*np.pi*f*t)
  noise = np.random.randn(fs)

  #各パワーの計算式
  #10*np.log10(np.sum(signal**2))
  #10*np.log10(np.sum(noise**2))

  snr = 6
  #snr=6となるnoiseの生成
  noise = noise/np.sqrt(np.sum(noise**2))
  noise = noise*np.sqrt(np.sum(signal**2))
  noise = noise*10**(-snr/20)

  #出力snr
  out_snr = 10*np.log10(np.sum(signal**2)/np.sum(noise**2))
  print('input_snr : {}'. format(snr))
  print('output_snr : {}'. format(out_snr))

  #混合
  x = signal+noise

  #plot
  plt.subplot(2, 1, 1)
  plt.title('dry_signal')
  plt.plot(t,signal)
  plt.subplot(2, 1, 2)
  plt.title('x')
  plt.plot(t,x)
  plt.show()


if __name__ == '__main__':

  task2_5()




