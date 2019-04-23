#the multiplication of sequence x[n] with the complex sequence is equal to the circular shift

from scipy import signal
import cmath
import numpy as np
import matplotlib.pyplot as plt
print("\n----TIME REVERSAL-----")

input('\nPress "manu" to Start:-')
input_amp=[1,2,3,4]#input_amp=x[n]
N=8
y=[]
j=cmath.sqrt(-1)
for n in range(0,(len(input_amp)-1)):
    sum=0
    for k in range(0,(len(input_amp)-1)):
        sum=sum+(input_amp[n]*np.exp(-j*2*3.14*k*n)/N)
    y.append(sum)
print("\ny",y)#y=x[k]:::::x[n]--dft-->x[k]
l=2
y[len(input_amp)-l]=[]
if(y[k]==y[len(input_amp)-l]):
  print("\n Time shifting property exists.....\n")
else:
  print("\n Time shifting property not exists.....\n")
print("\nBy MANASA J\n\n")



