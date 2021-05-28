import numpy as np
import matplotlib.pyplot as plt

def kakunin(t, x1, x2): 
	
	plt.figure()
	plt.subplot(2, 1, 1)
	plt.plot(t, x1)
	
	# 図の詳細（ラベル・軸など）の設定
	plt.title("x1") # タイトルの設定
	plt.xlabel("Time [s]") # 軸ラベルの設定
	plt.ylabel("Amplitude") # 軸ラベルの設定
	plt.ylim(0, 1) # 軸の表示範囲を設定
	plt.grid() # グリッドを表示
	
	plt.subplot(2, 1, 2)
	plt.plot(t, x2)
	
	# 図の詳細（ラベル・軸など）の設定
	plt.title("x2") # タイトルの設定
	plt.xlabel("Time [s]") # 軸ラベルの設定
	plt.ylabel("Amplitude") # 軸ラベルの設定
	plt.ylim(0, 1) # 軸の表示範囲を設定
	plt.grid() # グリッドを表示

	plt.tight_layout()
	plt.show()

def calculate_energy_centroid(t, x, fs):
	"""
	t: time
	x: signal
	fs: sampling rate
	
	return
	t_c: energy centroid
	"""
	energy = np.sum(x**2)/fs
	xx = x/np.sqrt(energy)
	#print("energy of x1 after normalization: {}".format(np.sum(xx**2)/fs))
	
	t_c = np.sum(t*xx**2)/fs
	
	return t_c

def calculate_duration(t, x, fs, t_c): 
	"""
	t: time
	x: signal
	fs: sampling rate
	t_c: energy centroid
	
	return
	sigma_t: duration
	"""
	energy = np.sum(x**2)/fs
	xx = x/np.sqrt(energy)
	t_c = sum(t*xx**2)/fs
	sigma_t = np.sum((t-t_c)**2*xx**2)/fs
	return sigma_t
	
def main(): 
	fs = 44100
	t = np.arange(fs).reshape((fs, 1))/fs # arangeはfs-1まで含む, 列ベクトルで統一
	
	x1 = np.zeros((fs, 1)) # タプル型の指定が必要
	x1[int(fs/2)-500+1:int(fs/2)+500+1]=1 # int型にキャスティングが必要
	
	x2 = np.zeros((fs, 1))
	x2[int(fs/4)-1000+1:int(fs/4)+1000+1]=1
	
	kakunin(t, x1, x2)

	t_c = calculate_energy_centroid(t, x1, fs)
	print('energy centroid: %.10f (Eq. 2.14)' % t_c)
		
	sigma_t = calculate_duration(t, x1, fs, t_c)
	print('duration       : %.10f (Eq. 2.15)' % sigma_t)
	
	# 式 (2.16) との比較
	t_c1 = calculate_energy_centroid(t, x1, fs)
	t_c2 = calculate_energy_centroid(t**2, x1, fs)
	
	sigma_t = t_c2-t_c1**2
	print('duration       : %.10f (Eq. 2.16)' % sigma_t)
	
	result = fs/np.sum(x1**2)/3*(2*(500.5/fs)**3)
	print('duraiotn       : %.10f (Eq. 2.17,2.18)' % result)
	
	
if __name__ == "__main__":
	main()
