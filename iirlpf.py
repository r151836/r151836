import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
z=[]
t=0.1
wp=0.35*np.pi
ws=0.7*np.pi
w1p=(2/t)*np.tan(wp*0.5)
w1s=(2/t)*np.tan(ws*0.5)
n1=np.log(w1s/w1p)
n2=(10**(0.1*20))-1
n3=(10**(0.1*4.436))-1
n=np.ceil((0.5*np.log(n2/n3))/n1)
wc1=((0.1**(-2))-1)**(0.5/n)
print(wc1)
wc=w1s/wc1
print(n)
print(wc)
b=2*(np.sin((1)*np.pi/(2*n)))	
print(b)
w=np.linspace(0,3.14,1000)
z1=np.exp(j*w)
z=np.append(z,z1)
s1=(1-(1/z))/(1+1/z)
s=(2/t)*s1
h1=s**2+b*wc*s+wc**2
h=wc**2/h1
plt.title("phase spectum")
plt.plot(w,np.abs(h))
plt.title("magnitude spectrum")
plt.plot(w,h)
plt.show()

 
