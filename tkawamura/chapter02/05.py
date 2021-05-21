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

def main(): 
	
	fs = 100
	t = np.arange(fs).reshape((fs, 1))/fs
	f = 1
	signal = np.sin(2*np.pi*f*t)
	noise = np.random.randn(fs, 1)
	
	print("power of signal: {} [dB]".format(10*np.log10(np.sum(signal**2))))
	print("power of signal: {} [dB]".format(10*np.log10(np.sum(noise**2))))

	snr = 6
	coeff = calculate_coefficient_from_snr(signal, noise, snr)
	noise = noise*coeff
	
	print("input SNR: {} [dB]".format(10*np.log10(np.sum(signal**2)/np.sum(noise**2))))
	

if __name__ == "__main__":
	main()