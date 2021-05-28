import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import math
import random
np.random.seed(seed=3)

def task3_7():
  N = 8
  x = np.random.random(N)
  c = np.zeros_like(x)

  #fft処理
  for k in range(N):#fの変動
    tmp_x = 0
    for n in range(N): #サンプル数
      tmp_x += x[n] * np.exp(-1j*2*np.pi*k*n/N)
    c[k] = tmp_x

  #npのfft
  X = np.fft.fft(x)

  #差分の表示
  plt.plot(X-c)
  plt.show()


if __name__ == '__main__':

  task3_7()