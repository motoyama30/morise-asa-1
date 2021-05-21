import numpy as np
import matplotlib.pyplot as plt

def main(): 

	N = 1000
	
	np.random.seed(42) # シードの設定，シード固定してもx1=x2とはならないことを確認
	x1 = np.random.randn(N, 1)
	x2 = np.random.randn(N, 1)
	#print("sum((x1 - x2)**2): {}".format(np.sum((x1-x2)**2)))
	
	# 直流成分の除去
	x1 = x1 - np.mean(x1)
	x2 = x2 - np.mean(x2)
	
	# パワーの計算，どちらも結果が同じことを確認
	L_p = 10*np.log10(np.sum(x1**2)/np.sum(x2**2)) # 信号長が同じ場合
	#L_p = 10*np.log10(np.mean(x1**2)/np.mean(x2**2)) # 信号長が異なる場合（平均）
	
	print("L_p: {}".format(L_p))

if __name__ == "__main__":
	main()