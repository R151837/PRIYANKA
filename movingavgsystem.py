import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
def mean(lst): return sum(lst)/len(lst)
fs,data=wav.read('swaarna.wav')
t=np.arange(0,len(data)/fs,1.0/fs)
noise=np.random.normal(0,10,data.shape)
plt.subplot(411)
plt.title('sin wave')
plt.plot(t,data)
a=list([data])
noise1=data+noise
plt.subplot(412)
plt.title('noise')
plt.plot(noise)
plt.subplot(413)
plt.title('noisy sin')
data=abs(data)
env=np.zeros_like(data)
for i in range(len(data))
	env[i]=mean(data[max(i-1000,0):i+1])
plt.subplot(414)
plt.title('mean average')
plt.plot(range(len(data)))
plt.show()
