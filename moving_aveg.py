import numpy as np
import matplotlib.pyplot as plt
p=int(input("enter the order of the moving average system:"))
Fs=1000
f1=10
f2=400
y=np.zeros(200)
#t=np.linspace(0,20,20)
t=np.linspace(0,400,200)
u=np.sin(2*np.pi*f1*t/Fs)

v=np.sin(2*np.pi*f2*t/Fs)

#x=[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
x=u+v

sum=0
q=p-1
for i in range(0,200,1):
	for k in range(0,q,1):
		sum=sum+x[i-k]
	print(sum)
	y[i]=float((sum)/(p))
	sum=0

print(y)
plt.subplot(411)
plt.plot(t,u)
plt.subplot(412)
plt.plot(t,v)
plt.subplot(413)
plt.plot(t,x)
plt.subplot(414)
plt.plot(t,y)
plt.show()
