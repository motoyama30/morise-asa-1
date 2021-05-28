import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import math

def task3_5():
  #定義
  fs = 44100
  t = np.arange(fs - 1)/fs
  #各周期，振幅，位相
  n1 = 1
  r1 = 1.5
  theta1 = 0.3
  n2 = 3
  r2 = 0.2
  theta2 = -1.1

  #観測信号
  x = r1*np.cos(2*np.pi*n1*t - theta1) + r2*np.cos(2*np.pi*n2*t - theta2)

  #周波数毎に計算
  k1 = 1
  c1 = np.sum(x * np.exp(-1j*2*np.pi*k1*t))/fs
  k3 = 3
  c3 = np.sum(x * np.exp(-1j*2*np.pi*k3*t))/fs

  print('accu_r1 : {}, est_r1 : {}' .format(r1, abs(c1) + np.conj(abs(c1))) )
  print('accu_r2 : {}, est_r2 : {}' .format(r2, abs(c3) + np.conj(abs(c3))) )

if __name__ == '__main__':

  task3_5()