import numpy as np


def MyHanning(N):
    n = np.arange(N)
    win = (1-np.cos(2*np.pi*n/(N-1)))/2
    return win


def MyHamming(N):
    n = np.arange(N)
    win = 0.54 - 0.46*np.cos(2*np.pi*n/(N-1))
    return win


def MyBlackman(N):
    n = np.arange(N)
    win = 0.42 - 0.5*np.cos(2*np.pi*n/(N-1)) + 0.08*np.cos(4*np.pi*n/(N-1))
    return win