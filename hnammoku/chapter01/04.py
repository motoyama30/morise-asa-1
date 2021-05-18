# 複素数
import numpy as np
# 複素数の例
x = 3 + 4j
print(x)
print(abs(x))
theta = np.degrees(np.angle(x))
print(theta)
# 複素数の実部と虚部
print(x.real)
print(x.imag)