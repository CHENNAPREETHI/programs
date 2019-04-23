import matplotlib.pyplot as plt
import numpy as np
p=complex(0,1)
x=[1,2,3,4,5,6]
N=1000
X=[]
w=np.linspace(-np.pi,np.pi,N-1)
for i in range(0,N-1):
	b=0
	for n in range(0,len(x)):
		b=b+(x[n]*np.exp(-n*2*np.pi*w[i]*p)/N)
	X.append(b)
plt.figure(1)
plt.plot(w,np.abs(X))
plt.xlabel('frequency')
plt.ylabel('magnitude')
plt.grid()
plt.figure(2)
plt.plot(w,np.angle(X))
plt.xlabel('frequency')
plt.ylabel('phase')
plt.grid()
plt.show()
