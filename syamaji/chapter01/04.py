
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import math

def task1_4(real, img):
  x = real + img*1j
  r = abs(x)
  theta = np.angle(x)

  print('r: {}' .format(r))
  print('theta: {}' .format(math.degrees(theta)))

if __name__ == '__main__':
  task1_4(0,1)

