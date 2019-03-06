import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs1,d8k=wav.read('nikhi1.wav')
fs2,d16k=wav.read('nikhi2.wav')
fs3,d2k=wav.read('nikhi3.wav')
print(fs1,len(d8k))
print(d8k)
t1=np.arange(0,len(d8k)/fs1,1.0/fs1)
t2=np.arange(0,len(d16k)/fs2,1.0/fs2)
t3=np.arange(0,len(d2k)/fs3,1.0/fs3)
plt.subplot(1,3,1)
plt.plot(t1,d8k)
plt.subplot(1,3,2)
plt.plot(t2,d16k)
plt.subplot(1,3,3)
plt.plot(t3,d2k)
plt.show()
