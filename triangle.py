import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
m=31
w=[]
for n in range(0,m):
	a=2*abs(n-((m-1)*0.5))/(m-1)
	y=1-a
	w=np.append(w,y)
print a
plt.stem(w)
plt.show()
	
