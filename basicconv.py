import numpy as np
import matplotlib.pyplot as plt
c[i]=0
for i in range(0,4):
    for j in range(i+1):
        c[i]=c[i]+a[j]*b[i-j]
print c[i]
