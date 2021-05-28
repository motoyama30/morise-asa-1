import numpy as np
import matplotlib.pyplot as plt

def main(): 
	
	fs = 44100  # 標本化周波数 [Hz]
	t = np.arange(fs/2-1)/fs  # 時間インデックス [秒]
	x = np.sin(2*np.pi*t) # 波形（正弦波)
	
	# 波形の描画（確認用）
	plt.figure()
	plt.plot(t, x)
	plt.show()

	S = sum(x)/fs # 区分求積法
	print("S =  {}".format(S))
	
if __name__ == "__main__":
	main()