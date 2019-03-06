import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x=input('enter sequence=')
n=len(x)
j=cm.sqrt(-1)
w=np.linspace(0,2*np.pi,1000)
y=[]
for i in range(0,1000):
	sum=0
	for k in range(0,n):
		sum=sum+x[k]*np.exp(-j*w[i]*k)
	y=np.append(y,sum)
print y
plt.subplot(121)
plt.title("magnitude")
plt.plot(w,np.abs(y))
plt.subplot(122)
plt.title("phase")
plt.plot(w,np.angle(y))
plt.show()
