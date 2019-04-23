from scipy import signal
import cmath
import numpy as np
import matplotlib.pyplot as plt
input_amp=[1,2,3,4]
N=8
y=[]
j=cmath.sqrt(-1)
for n in range(0,(len(input_amp)-1)):
	sum=0
	for k in range(0,(len(input_amp)-1)):
		sum=sum+(input_amp[n]*np.exp(-j*2*3.14*k*n)/N)
	y.append(sum)
print("\ny[k]\n",y)
input_amp1=[1,2,3,4]
N=8
y1=[]
j=cmath.sqrt(-1)
for n in range(0,(len(input_amp)-1)):
	sum1=0
	for k in range(0,(len(input_amp)-1)):
		sum1=sum1+(input_amp[n]*np.exp(-j*2*3.14*k*n)/N)
	y1.append(sum1)
print("\ny1[k]\n",y1)
y3=[]
y3=y1[k]*y[k]
print("\ny3[k]\n",y3)
if(y1[k]*y[k]==y3):
	print("\ncircular convolution exists...\n")
else:
	print("\ncircular convolution not exists...\n")
