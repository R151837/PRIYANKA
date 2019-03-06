import matplotlib.pyplot as plot
import numpy as np
t=np.arange(0,10,0.1)
x1=np.cos(t*2*np.pi)
plot.plot(t,x1)
plot.title('cos wave')
plot.xlabel('time')
plot.ylabel('amp')
plot.show( )
