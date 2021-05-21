import numpy as np
import matplotlib.pyplot as plt

def main(): 
	"""
	式 (2.6) の確認
	"""
	
	n = np.arange(20)
	omega = 0.1*2*np.pi
	
	x1 = np.sin(omega*n) 
	x2 = np.sin((omega+2*np.pi)*n)


	### 波形の比較（波形） ###
	
	plt.figure()
	
	# sin(ωn)のプロット
	plt.subplot(2, 1, 1)
	plt.plot(n, x1)
	
	# 図の詳細（ラベル・軸など）の設定
	plt.title("sin(ωn)") # タイトルの設定
	plt.xlabel("Time [sample]") # 軸ラベルの設定
	plt.ylabel("Amplitude") # 軸ラベルの設定
	plt.ylim(-1, 1) # 軸の表示範囲を設定
	plt.grid() # グリッドを表示
	
	# sin( (ω+2π) n)のプロット
	plt.subplot(2, 1, 2)
	plt.plot(n, x2)
	
	# 図の詳細（ラベル・軸など）の設定
	plt.title("sin( (ω+2π) n)") # タイトルの設定
	plt.xlabel("Time [sample]") # 軸ラベルの設定
	plt.ylabel("Amplitude") # 軸ラベルの設定
	plt.ylim(-1, 1) # 軸の表示範囲を設定
	plt.grid() # グリッドを表示

	plt.tight_layout()
	plt.show()
	
	### 波形の比較（誤差） ##
	
	plt.figure()
	
	# レンジ設定なし
	plt.subplot(2, 1, 1)	
	plt.plot(n, x1-x2)

	plt.title("error (w/o setting measurement range)") # タイトルの設定
	plt.xlabel("Time [sample]") # 軸ラベルの設定
	plt.ylabel("Amplitude") # 軸ラベルの設定
	#plt.ylim(-1, 1) # 軸の表示範囲を設定

	plt.subplot(2, 1, 2)	
	plt.plot(n, x1-x2)
	
	# 図の詳細（ラベル・軸など）の設定
	plt.title("error (w setting measurement range)") # タイトルの設定
	plt.xlabel("Time [sample]") # 軸ラベルの設定
	plt.ylabel("Amplitude") # 軸ラベルの設定
	plt.ylim(-1, 1) # 軸の表示範囲を設定
	
	plt.tight_layout()
	plt.show()

if __name__ == "__main__":
	main()