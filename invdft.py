import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
def idft(x):
	y=[]
	n=len(x)
	k=np.linspace(0,N-1,N)
	for i in range(0,N):
		sum=0
		for n in range(0,len(x)):
			sum=sum+x[n]*np.exp((n*2*np.pi*k[i]*j)/N)	
		y.append(sum/N)
	return(y)
N=4
x=input('sequence:')
x1=idft(x)
plt.plot(x1)
plt.show()

