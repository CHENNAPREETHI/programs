import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x=[0,1,2,3,4,5]
N=1000
X=[]
k=complex(0,-1)
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,N): 
	s=0
	for n in range(0,len(x)):
        	s=s+(x[n]*np.exp(k*w[i]*n))
	X.append(s)
plt.subplot(141)	
plt.plot(w,X)
plt.subplot(142)
m=np.abs(X)
plt.plot(w,m)
plt.subplot(143)
p=np.angle(X)
plt.plot(w,p)
plt.subplot(144)
plt.plot(x)
plt.show()
