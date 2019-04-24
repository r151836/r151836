import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
n=np.arange(0,31)
w=[]
N=31
for n in range(0,31):
	w1=0.5-(0.46*np.cos((2*np.pi*n)/(N-1)))
	w=np.append(w,w1)
plt.stem(w)
plt.show()
