#without using function#
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
y=[]
x=input('enter sequence')
n=len(x)
N=10000
w=np.linspace(0,2*np.pi,N)
for i in range(0,N):
	w_1=w[i]
	sum=0
	for k in range(0,n):
		sum=sum+(x[k]*np.exp(-k*w_1*j))
	y.append(sum)
plt.plot(y)
plt.subplot(2,1,1)
plt.plot(w,np.abs(y))
plt.xlabel('freq(w/pi)')
plt.ylabel('magnitude')
plt.title('magnitude spectrum')
plt.grid()
plt.subplot(4,1,2)
plt.plot(w,np.angle(y))
plt.xlabel('freq(w)')
plt.ylabel('phase angle in radian')
plt.title('phase spectrum')
plt.grid()
plt.subplot(4,2,3)
plt.plot(w,y)
plt.xlabel('freq(w/pi)')
plt.ylabel('real part')
plt.title('real values of x')
plt.grid()
plt.subplot(4,2,4)
plt.plot(w,np.imag(y))
plt.xlabel('freq(w/pi)')
plt.ylabel('imaginary part')
plt.title('imaginary values of x')
plt.grid()
plt.show()
    
