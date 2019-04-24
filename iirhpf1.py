import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
z=[]
t=0.1
ws=0.35*np.pi
wp=0.7*np.pi
w1p=(2/t)*np.tan(wp*0.5)
w1s=(2/t)*np.tan(ws*0.5)
print w1p,'w1p'
print w1s,'w1s'
w2p=1
w2s=w1p/w1s
print (w2s,'w2s')
n1=np.log(w2s/w2p)
ss=0.1**2
sp=0.6**2
n2=(1/ss)-1
n3=(1/sp)-1
n4=0.5*np.log(n2/n3)
n=np.ceil(n4/n1)
print(n)
wc1=((1/ss)-1)**(1/2*n)
wc=w2s/wc1
print(wc,'wc')
b=2*(np.sin(np.pi/(4)))	
print(b)
w=np.linspace(0,3.14,10000)
z1=np.exp(j*w)
z=np.append(z,z1)
s1=(1-(1/z))/(1+1/z)
s2=(2/t)*s1
s=w1p/s2
h1=s**2+b*wc*s+wc**2
h2=wc**n
h=h2/h1
plt.figure(1)
plt.title("phase spectum")
plt.plot(w,np.abs(h))
plt.figure(2)
plt.title("magnitude spectrum")
plt.plot(w,h)
plt.show()

