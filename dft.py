import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
j=cm.sqrt(-1)
x=input('enter seq1 x=')
N=len(x)
y=[]
for n in range(0,N):
	sum=0
	for k in range(0,N):
		sum=sum+(x[k]*np.exp((-j*2*np.pi*n*k)/N))
	y=np.append(y,sum)
print y
plt.stem(np.abs(y))
plt.show()
