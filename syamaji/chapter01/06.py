
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import math

def task1_6():
  #x,hを定義
  x = np.array([1,3,-5,2],dtype =float)
  h = np.array([1,2,1],dtype =float)
  #convを計算
  y = np.convolve(x,h)
  print('conv(x,h): {}' .format(y))

  t = range(y.shape[0])
  plt.plot(t,y)
  plt.show()

if __name__ == '__main__':
  task1_6()





