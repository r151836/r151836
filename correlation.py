import numpy as np
n=input("enter the lentght")
m=input("enter the length")
x=np.zeros(n)
h=np.zeros(m)
h1=np.zeros(m)
y=np.zeros(n+m-1)
print('enter the elements of x:')
for j in range(0,n):
	x[j]=input("enter number")
print(x)
print('enter the elements of h:')
for j in range(0,m):
	h[j]=input("enter number")
print(h)
print('reverse of the h:')
for i in range(m):
	#h1.append(0)
	h1[i]=h[-i-1]
print(h1)
for i in range(0,n+m-1):
	su=0
   	for k in range(0,n):
        		if (i-k>=0 and i-k<m):
        			su=su+x[k]*h1[i-k]
   			y[i]=su
print('corelation:')
print y
