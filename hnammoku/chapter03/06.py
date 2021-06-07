import numpy as np

fs = 8
r = 0.5
print(f"fs = {fs} のとき")
for f in range(fs):
    t = np.arange(fs) / fs
    x = r * np.cos(2 * np.pi * f * t)
    c = np.sum(x * np.exp(-1j * 2 * np.pi * f * t)) / fs
    print(f"振幅（f = {f}）: {np.abs(c)}")

fs = 7
print(f"fs = {fs} のとき")
for f in range(fs):
    t = np.arange(fs) / fs
    x = r * np.cos(2 * np.pi * f * t)
    c = np.sum(x * np.exp(-1j * 2 * np.pi * f * t)) / fs
    print(f"振幅（f = {f}）: {np.abs(c)}")
