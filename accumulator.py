import numpy as np
from matplotlib import pyplot as plt
t=np.linspace(0,0.01,100)
n=np.linspace(-10,10,20)
f=input("Enter a low frequency(Hz):")
f=f*1.0
fs=input("Enter a high frequency(Hz):")
fs=fs*1.0

x=np.sin(2*np.pi*(f/fs)*n)
plt.subplot(224)
plt.stem(n,x)
plt.show()
p=input("Enter current sample value:")
s=0
i=0
for i in range(p):
    s=s+x[i]
    print("Sum of first %d Samples is: %f" %(i,s))
print ("Final acumulator output is:%f"%(s))
