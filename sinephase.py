import matplotlib.pyplot as plot
import numpy as np
t=np.arange(0,10,0.1)
x1=np.sin(t*2*np.pi)
plot.plot(t,x1)
plot.title('sine wave')
plot.xlabel('time')
plot.ylabel('amp')
x2=np.cos(t*2*np.pi+(np.pi)/2)
plot.plot(t,x2)
plot.title('sine phase wave')
plot.xlabel('time')
plot.ylabel('amp')
plot.show( )
