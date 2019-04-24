import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
wh=[]
m=31
for n in range(0,m):
	p=0.5*np.cos((2*np.pi*n)/(m-1))
	y=0.5-p
	wh=np.append(wh,y)
plt.stem(wh)
plt.show()
	

