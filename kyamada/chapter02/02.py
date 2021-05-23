import numpy as np
import matplotlib.pyplot as plt

n = np.arange(20)
omega = 0.1*2*np.pi
x1 = np.sin(omega*n)
x2 = np.sin((omega+2*np.pi)*n)

# グラフの表示(1)
plt.subplot(2,1,1)
plt.plot(n,x1)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("sin(wn) ")

plt.subplot(2,1,2)
plt.plot(n,x2)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("sin((w+2π)n)")
plt.tight_layout() # グラフタイトルが重ならないようにする
plt.show()

# グラフの表示(2 誤差)
plt.subplot(2,1,1)
plt.plot(n,x2-x1) # x2-x1で誤差を計測する
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("error (w/o setting measurement range)")

#  軸の表示範囲を設定したとき
plt.subplot(2,1,2)
plt.plot(n,x2-x1)
plt.ylim(-1, 1) # 軸の表示範囲を設定
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("error (w setting measurement range)")
plt.tight_layout()
plt.show()