
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

def task1_2():
  #定義
  x = np.array([1,3,-5,2],dtype=float)
  y = np.array([1,3,-5,2],dtype=float)

  #Calcu
  #inner_p = np.dot(x,y)
  inner_p = x @ y
  print('Inner product: {}' .format(inner_p))

def task1_3():
  #定義
  fs = 44100
  f =1
  t = np.linspace(0, 1, fs)
  x = np.sin(2*np.pi*f*t)

  #plot
  plt.plot(t,x)
  plt.show()

def task1_4(real, img):
  x = real + img*1j
  r = abs(x)
  theta = np.angle(x)

  print('r: {}' .format(r))
  print('theta: {}' .format(math.degrees(theta)))

def task1_5():
  np_x = np.exp(1j*np.pi/2)
  np_y = np.exp(1j*np.pi)
  np_z = np.exp(1j*np.pi*2)

  print('np_x: {}' .format(np_x))
  print('np_y: {}' .format(np_y))
  print('np_z: {}' .format(np_z))

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

#def impulse_responce():
# ##############
#  # x: imp
#  # y: imp res
#  ##############
#  x = np.array([0,0,2,0,0,0,0],dtype =float)
#  h = np.arange(10,0,-2)/10
#  y = np.convolve(x,h)
#  t = range(y.shape[0])

#  #plot
#  plt.plot(t,y)
#  plt.show()

if __name__ == '__main__':

  #task1_1()
  #task1_2()
  #task1_3()
  #task1_4(0,1)
  #task1_5()
  task1_6()





