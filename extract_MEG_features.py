#script to extract dyadic features from MEG data
import numpy as np
from scipy.io import loadmat
from scipy.io import savemat
#import matplotlib.pyplot as plt
import sys

block=sys.argv[1] # np.arange(1,9)

meg_data = loadmat(f'block{block}.mat')['data']
windows=[25,12,6,3] #250ms, 120ms, 60ms, 30ms
fs=100

n_channels=meg_data.shape[1] #should be 157
n_points=int(meg_data.shape[0]) #should be ~90000 samples = ~15min @100hz
n_windows=len(windows)

meg_features=np.zeros( (n_points,n_channels,n_windows) )

for c,channel in enumerate(np.arange(n_channels)):
    print(f'channel {c}')
    for w,window in enumerate(windows):
        print(f'window {w}')
        #corner_freq=1/window
        band=np.zeros(n_points)
        for n in np.arange(n_points):
            b=n
            e=b+window
            band[n]=np.mean(meg_data[:,channel][b:e])
        meg_features[:,c,w]=band
        # plt.figure()
        # plt.plot(band[0:1000])
        # plt.title(f"window={window}")
meg_features=meg_features.reshape(n_points,n_channels*n_windows)
savemat(f'meg_features_block{block}.mat', {'data': meg_features})