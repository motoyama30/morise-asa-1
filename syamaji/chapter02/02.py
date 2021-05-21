
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import math

def task2_2():
  #定義
  n = np.arange(0,21)
  omega = 0.1*2*np.pi
  x1 = np.sin(omega*n)
  x2 = np.sin((omega+2*np.pi)*n)

  #波形表示
  plt.subplot(2, 2, 1)
  plt.title('sin(ωn)')
  plt.plot(n,x1)
  plt.grid()
  plt.subplot(2, 2, 2)
  plt.title('sin((ω+2π)n)')
  plt.plot(n,x2)
  plt.xlabel('N')
  plt.grid()
  #plt.show()

  #誤差表示
  plt.subplot(2, 2, 3)
  plt.title('Error')
  plt.plot(n,x1-x2)
  plt.grid()
  plt.subplot(2, 2, 4)
  plt.title('Error set range')
  plt.plot(n,x1-x2)
  plt.grid()
  plt.ylim( -1, 1 )
  plt.tight_layout()
  plt.show()

if __name__ == '__main__':
  task2_2()




