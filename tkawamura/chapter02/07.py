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
	

def kakunin(t, s, x, y_moving_average, y_median):
	"""
	波形の比較
	t: time
	s: signal
	x: signal+noise
	y_moving_average: estimated signal	(移動平均フィルタ)
	y_median: estimated signal	(メディアンフィルタ)
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
	
	# y[n] :移動平均
	plt.subplot(3, 1, 2)
	plt.plot(t, s, linestyle = "dashed")
	plt.plot(t, y_moving_average)
	
	# 図の詳細（ラベル・軸など）の設定
	plt.title("y[n]: estimated signal (moving average filter)") # タイトルの設定
	plt.xlabel("Time [sample]") # 軸ラベルの設定
	plt.ylabel("Amplitude") # 軸ラベルの設定
	plt.ylim(-2, 2) # 軸の表示範囲を設定
	plt.grid() # グリッドを表示

	# y[n]: メディアン
	plt.subplot(3, 1, 3)
	plt.plot(t, s, linestyle = "dashed")
	plt.plot(t, y_median, label="signal+noise")
	
	# 図の詳細（ラベル・軸など）の設定
	plt.title("y[n]: estimated signal (median filter)") # タイトルの設定
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

	# パルス状ノイズの作成
	noise = np.zeros((fs, 1))
	number_of_pulses = 5
	for i in range(number_of_pulses):
  		noise[np.random.randint((np.size(noise)))] = 2*np.round(np.random.rand()) - 1
	
	snr = 6
	coeff = calculate_coefficient_from_snr(signal, noise, snr)
	noise = noise*coeff
	
	x = signal + noise

	y_moving_average = np.zeros((len(x), 1)) # length は　len sizeなどに変換
	M = 5
	for i in [i for i in range(M, len(y_moving_average)-M+1)]: 
		y_moving_average[i] = np.mean(x[i-M:i+M])
	
	y_median = np.zeros((len(x), 1)) # length は　len sizeなどに変換
	M = 5
	for i in [i for i in range(M, len(y_median)-M+1)]: 
		y_median[i] = np.median(x[i-M:i+M])
	
	kakunin(t, signal, x, y_moving_average, y_median)
	
	print("input SNR: {} [dB]".format(10*np.log10(np.sum(signal**2)/np.sum(noise**2))))
	print("output SNR (moving average): {} [dB]".format(10*np.log10(np.sum(signal**2)/np.sum((y_moving_average-signal)**2))))
	print("output SNR (median): {} [dB]".format(10*np.log10(np.sum(signal**2)/np.sum((y_median-signal)**2))))


if __name__ == "__main__":
	main()