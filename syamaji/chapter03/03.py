
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import math

def task3_3():
  #定義
  fs = 44100
  r = 1.5
  theta = 0.3
  f = 2
  n = 2
  m = 3
  t = np.arange(fs - 1)/fs

  #観測信号
  x = r*np.cos(2*np.pi*n*t - theta)

  # sin cosの係数計算
  a = 2/fs*np.sum(np.dot(x, np.cos(2*np.pi*m*t)))
  b = 2/fs*np.sum(np.dot(x, np.sin(2*np.pi*m*t)))

  # n!=mのため，大体0　直交性
  print('a : {}' .format(a))
  print('b : {}' .format(b))

if __name__ == '__main__':

  task3_3()
