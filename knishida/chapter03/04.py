import numpy as np


# declare
fs = 44100
n1 = 1
r1 = 1.5
theta1 = 0.3
n2 = 3
r2 = 0.3
theta2 = 1.1
t = np.arange(0, 1, 1 / fs)
x = np.array(
    r1 * np.cos(2 * np.pi * n1 * t - theta1) + r2 * np.cos(2 * np.pi * n2 * t - theta2)
)

# calc about a,b
a1 = 2 / fs * np.sum(x * np.cos(2 * np.pi * n1 * t))
b1 = 2 / fs * np.sum(x * np.sin(2 * np.pi * n1 * t))
a2 = 2 / fs * np.sum(x * np.cos(2 * np.pi * n2 * t))
b2 = 2 / fs * np.sum(x * np.sin(2 * np.pi * n2 * t))

# check
r1_c = np.sqrt(a1 ** 2 + b1 ** 2)
theta1_c = np.arctan2(b1, a1)
r2_c = np.sqrt(a2 ** 2 + b2 ** 2)
theta2_c = np.arctan2(b2, a2)

# output
print(f"r1:{r1_c}")
print(f"theta1:{theta1_c}")
print(f"r2:{r2_c}")
print(f"theta2:{theta2_c}")
