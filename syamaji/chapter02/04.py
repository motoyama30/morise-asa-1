
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import math

def task2_4():
  #定義
  fs =44100
  t = np.arange(fs)/fs

  x1 = np.zeros(fs, dtype=float)
  #index指定はintで
  x1[fs//2-500+1 : fs//2+500+1] = 1
  x2 = np.zeros(fs, dtype=float)
  x2[fs//4-1000+1 : fs//4+100+1] = 1

  plt.subplot(2, 2, 1)
  plt.title('x1')
  plt.plot(t,x1)
  plt.grid()
  plt.subplot(2, 2, 2)
  plt.title('x2')
  plt.plot(t,x2)
  plt.grid()
  #plt.show()

  #信号の正規化
  energy =np.sum(x1**2)/fs
  xx1 = x1/np.sqrt(energy)
  print(np.sum(xx1**2)/fs)

  #平均時間
  t_c = np.sum(t*xx1**2)/fs

  #eq1
  sigma_t1= np.sum((t-t_c)**2 * xx1**2)/fs

  #eq2
  t_c1 = np.sum(   t * xx1**2)/fs
  t_c2 = np.sum(t**2 * xx1**2)/fs
  sigma_t2 = t_c2 - t_c1**2

  #eq3
  sigma_t3 = (fs/np.sum(x1**2))/3 * (2*(500.5/fs)**3)

  print('平均時間 : {}' .format(t_c))
  print('eq1 : {}' .format(sigma_t1))
  print('eq2 : {}' .format(sigma_t2))
  print('eq3 : {}' .format(sigma_t3))


if __name__ == '__main__':
  task2_4()




