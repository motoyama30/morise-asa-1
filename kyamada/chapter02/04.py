import numpy as np

# 信号の生成
fs = 44100
t = np.arange(fs).reshape((fs, 1))/fs # 縦ベクトルにする必要がある！！
print(t.shape)
x1 = np.zeros((fs,1))
x2 = np.zeros((fs,1))

# スライスして、fs/2サンプルの前後500こを1にする




x1[int(fs/2-500):int(fs/2+500+1)] = 1
# x2は、前後1000サンプルを1にする
x2[int(fs/2-1000):int(fs/2+1000+1)] = 1

# 配列サイズの確認
print(f'size of array (before) : {x1[int(fs/2-500):int(fs/2+500)].shape}')
print(f'size of array (after)  : {x1[int(fs/2-500):int(fs/2+500+1)].shape}')

"""
スライス位置、[int(fs/2-500):int(fs/2+500)]の時
(1) engry_centroid : 0.49998866213151927
(2) duration :0.00004284904437965662
(3) duration :0.00004284904437965031
(4) duration :0.00004297776308054085

スライス[int(fs/2-500):int(fs/2+500+1)]のとき
(1) engry_centroid : 0.5000000000000001
(2) duration :0.00004293478540320134
(3) duration :0.00004293478540307039
(4) duration :0.00004293482825228856

0.5を中心に、1001個数の1が並んでいるため、中心がちょうど、500個,1個,500個となる。
よって平均時間は0.5になる。
"""
#print(x1)
#plt.plot(t,x1)
#plt.show() # 0.5あたりにパワーが集中していることがわかった。→求めたい値、重心

# 前提条件が必要(信号のエネルギーが1である)
engry = np.sum(x1**2)/fs #->1であって欲しいから
xx1 = x1/np.sqrt(engry)
print(np.sum(xx1**2/fs)) # 1になってればOK

# 1の式から求める（区分求積法）

engry_centroid = np.sum(t*xx1**2)/fs
print(f'(1) engry_centroid : {engry_centroid}')
# 出力 (1) engry_centroid : 0.49998866213151927

# 平均時間を求める(2)
sigma = np.sum((t-engry_centroid)**2*xx1**2)/fs
print('(2) duration :' + str('{:.20f}'.format(sigma)))

# 平均時間を求める(3)
t_c2 = np.sum(t**2 * xx1**2)/fs # t^2
sigma_3 = t_c2 - engry_centroid**2
print('(3) duration :' + str('{:.20f}'.format(sigma_3)))

# 平均時間を求める(4)近似の方法
sigma_4 = fs/np.sum(x1**2)/3 * (2 * (500.5/fs)** 3)
print('(4) duration :' + str('{:.20f}'.format(sigma_4)))
