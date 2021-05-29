import numpy as np


# declare
fs = 44100
n1 = 1
r1 = 1.5
theta1 = 0.3
n2 = 3
r2 = 0.2
theta2 = -1.1
t = np.arange(0, 1, 1 / fs)
x = np.array(
    r1 * np.cos(2 * np.pi * n1 * t - theta1) + r2 * np.cos(2 * np.pi * n2 * t - theta2)
)

# calc about c
k1 = 1
c1 = np.sum(x * np.exp(-1j * 2 * np.pi * k1 * t)) / fs
k3 = 3
c3 = np.sum(x * np.exp(-1j * 2 * np.pi * k3 * t)) / fs

# check
r1_c = np.abs(c1)
theta1_c = np.angle(np.conj(c1))
r2_c = np.abs(c3)
theta2_c = np.angle(np.conj(c3))

# output
print(f"r1:{r1_c}")
print(f"theta1:{theta1_c}")
print(f"r2:{r2_c}")
print(f"theta2:{theta2_c}")
