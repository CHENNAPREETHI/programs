import numpy as np
from matplotlib import pyplot as plt
def convolution(x,h):
	lx=len(x)
	lh=len(h)
	y=[]
	for n in range(lx+lh-1):
		sum=0
		for k in range(lx):
			if((n-k)<lx and (n-k)>=0):
				sum=sum+x[k]*h[n-k]
		y=np.append(y,sum)
	return y
def time_rev(x):
	lx=len(x)
	y=[]
	for i in range(0,lx):
		y=np.append(y,x[lx-i-1])
	return y
x=np.array(input("enter sequence 1:"))
x=np.array(input("enter sequence 2:"))
print(convolute(x,h))
print("conv=",np.convolve(x,h))
print(convolute(x,time_rev(h)))

n=np.arrange(0,500)
x=np.sin(2*np.pi*20.0/400.0*n)
N=np.sin(2*np.pi*50.0/400.0*n)
N1=np.random.rand(x.shape[0])
x_N=np.x+N+N1
h=[1.0/3.0,1.0/3.0,1.0/3.0]
y1=convolute(h,x_N)
y2=convolute(x,time_rev(x))#autocorrelation(x)
y3=convolute(x_N,time_rev(x_N))#autocorrelation(x_N)



