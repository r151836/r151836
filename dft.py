import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dft(x):
	j=cm.sqrt(-1)
	y=[]
	n=len(x)
	k=np.linspace(0,N-1,N)
	for i in range(0,N):
		sum=0
		for n in range(0,len(x)):
			sum=sum+(x[n]*np.exp((-n*2*np.pi*k[i]*j)/N))
		y.append(sum)
	return y
N=4
x=input('x sequence:')
x1=dft(x)
print (x1)
h=input('h sequence:')
h1=dft(x)
print(h1)
n=len(x)
y=[]
for i in range(0,n):
	sum=0
	sum=sum+h1[i]*x1[i]
	y.append(sum)
print(y)
plt.plot(y)
plt.show()

