import numpy as np
n=input("enter the lentght")
m=input("enter the length")
x=np.zeros(n)
h=np.zeros(m)
y=np.zeros(n+m-1)
print('enter the elements of x:')
for j in range(0,n):
    x[j]=input("enter number")
print('enter the elements of h:')
for j in range(0,m):
   h[j]=input("enter number")
for i in range(0,n+m-1):
   su=0
   for k in range(0,n):
        if (i-k>=0 and i-k<m):
        	su=su+x[k]*h[i-k]
   y[i]=su
print y


	
