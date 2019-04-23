import matplotlib.pyplot as plt
import numpy as np
p=complex(0,1)
x1=[1,2,3,4,5,6]
x2=[2,4,6]
N=1000
X1=[]
X2=[]
w=np.linspace(-np.pi,np.pi,N-1)
for i in range(0,N-1):
	b1=0
	for n in range(0,len(x1)):
		b1=b1+(x1[n]*np.exp(-n*2*np.pi*w[i]*p)/N)
	X1.append(b1)
for j in range(0,N-1):
	b2=0
	for n in range(0,len(x2)):
		b2=b2+(x2[n]*np.exp(-n*2*np.pi*w[j]*p)/N)
	X2.append(b2)
X=X1+X2
plt.subplot(311)
plt.plot(w,X1)
plt.subplot(312)
plt.plot(w,X2)
plt.subplot(313)
#plt.plot(w,X)
plt.show()
