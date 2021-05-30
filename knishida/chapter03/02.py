import numpy as np


# declare
fs = 44100
r = 1.5
theta = 0.3
f = 2
L = 1 / f
t = np.arange(0, L, 1 / fs)
x = np.array(r * np.cos(2 * np.pi * t / L - theta))

# caluculate about a,b
a = 2 / fs / L * np.sum(x * np.cos(2 * np.pi * t / L))
b = 2 / fs / L * np.sum(x * np.sin(2 * np.pi * t / L))

# check
r_c = np.sqrt(a ** 2 + b ** 2)
theta_c = np.arctan2(b, a)

# output
print(f"a:{a}")
print(f"b:{b}")
print(f"r:{r_c}")
print(f"theta:{theta_c}")
