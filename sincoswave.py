import matplotlib.pyplot as plot
import numpy as np
t=np.arange(0,10,1)
x1=np.sin(5*np.pi*t)
plot.subplot(1,3,1)
plot.stem(t,x1)
plot.title('sin wave')
plot.xlabel('time')
plot.ylabel('amp')
x2=np.cos(6*np.pi*t)
plot.subplot(1,3,2)
plot.stem(t,x2)
plot.title('cos wave')
x=x1+x2
plot.subplot(1,3,3)
plot.stem(t,x)
plot.title('addition of sine and cos')
plot.show( )
