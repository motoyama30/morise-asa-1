import numpy as np
np.random.seed(0) # シード値

# ホワイトノイズの作成
N = np.arange(1000) # 信号長
x1 = np.random.randn(len(N),1)
x2 = np.random.randn(len(N),1)

#plt.plot(N,x1)
#plt.show()

# 直流成分を削除する
x1 = x1 - np.mean(x1)
x2 = x2 - np.mean(x2)

# パワー比について形式3の式を使って比較する
L_p = 10*np.log10(np.sum(x1**2)/np.sum(x2**2))
print(f'L_p : {L_p}')
# 出力: L_p : 0.16769228784400791
