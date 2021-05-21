import numpy as np
import matplotlib.pyplot as plt

def calculate_coefficient_from_snr(signal, noise, snr): 
	"""
	signal: signal
	noise: noise
	snr: input SNR
	
	return:
	coeff: coefficient of noise
	"""

	pow_s = np.sqrt(np.sum(signal**2))
	pow_n = np.sqrt(np.sum(noise**2))
	coeff = pow_s/pow_n*10**(-snr/20)
	
	return coeff

def kakunin(t, s, x, y):
	"""
	波形の比較
	t: time
	s: signal
	x: signal+noise
	
	return:
	y: estimated signal
	"""
	
	plt.figure()
	
	# s[n]
	plt.subplot(3, 1, 1)
	plt.plot(t, s)
	
	# 図の詳細（ラベル・軸など）の設定
	plt.title("s[n]: signal") # タイトルの設定
	plt.xlabel("Time [s]") # 軸ラベルの設定
	plt.ylabel("Amplitude") # 軸ラベルの設定
	plt.ylim(-2, 2) # 軸の表示範囲を設定
	plt.grid() # グリッドを表示
	
	# x[n]
	plt.subplot(3, 1, 2)
	plt.plot(t, s, linestyle = "dashed")
	plt.plot(t, x, label="signal+noise")
	
	# 図の詳細（ラベル・軸など）の設定
	plt.title("x[n]: signal+noise") # タイトルの設定
	plt.xlabel("Time [sample]") # 軸ラベルの設定
	plt.ylabel("Amplitude") # 軸ラベルの設定
	plt.ylim(-2, 2) # 軸の表示範囲を設定
	plt.grid() # グリッドを表示

	# y[n]
	plt.subplot(3, 1, 3)
	plt.plot(t, s, linestyle = "dashed")
	plt.plot(t, y)
	
	# 図の詳細（ラベル・軸など）の設定
	plt.title("y[n]: estimated signal") # タイトルの設定
	plt.xlabel("Time [sample]") # 軸ラベルの設定
	plt.ylabel("Amplitude") # 軸ラベルの設定
	plt.ylim(-2, 2) # 軸の表示範囲を設定
	plt.grid() # グリッドを表示

	plt.tight_layout()
	plt.show()


def main(): 

	fs = 100
	t = np.arange(fs).reshape((fs, 1))/fs
	f = 1
	signal = np.sin(2*np.pi*f*t)
	noise = np.random.randn(fs, 1)
	
	snr = 6
	coeff = calculate_coefficient_from_snr(signal, noise, snr)
	noise = noise*coeff
	
	x = signal + noise
	
	y = np.zeros((len(x), 1)) # length は　len sizeなどに変換
	M = 5
	for i in [i for i in range(M, len(y)-M+1)]: 
		y[i] = np.mean(x[i-M:i+M])
	
	kakunin(t, signal, x, y)
	
	print("input SNR: {} [dB]".format(10*np.log10(np.sum(signal**2)/np.sum(noise**2))))
	print("output SNR: {} [dB]".format(10*np.log10(np.sum(signal**2)/np.sum((y-signal)**2))))


if __name__ == "__main__":
	main()
