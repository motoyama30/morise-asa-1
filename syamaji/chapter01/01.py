
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import math

def task1_1():
  #定義
  x = np.array([1,3,-5,2],dtype=float)
  fs =10
  t = np.arange(0,x.shape[0])/fs
  #plot
  plt.plot(t,x)
  plt.show()


if __name__ == '__main__':

  task1_1()




