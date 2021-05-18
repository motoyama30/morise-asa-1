
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import math


def task1_3():
  #定義
  fs = 44100
  f =1
  t = np.linspace(0, 1, fs)
  x = np.sin(2*np.pi*f*t)

  #plot
  plt.plot(t,x)
  plt.show()


if __name__ == '__main__':

  task1_3()





