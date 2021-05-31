import numpy as np

c = complex(3, 4)  # 関数を使うとき

x = 3 + 4j
r = abs(x)

print(x)
print(r)
# 偏角を求める
angle = np.angle(x)
print(angle)
theta = np.degrees(angle)
print(theta)

print(x.real)
print(x.imag)

print(c.real)
print(c.imag)
