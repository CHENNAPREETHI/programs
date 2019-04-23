from scipy import signal
import cmath
import numpy as np
import matplotlib.pyplot as plt
print("\n----LINEARITY PROPERTY-----")

input('\nPress "manu" to Start:-')
a1=3
a2=5
x1=[2,3,5,8,9,22,56,7]
x2=[32,1,9,10,45]
#o/p
y1=[]
y2=[]
j=cmath.sqrt(-1)
#apply dft for x1 and x2
#y1=x1[k],y2=x2[k]
N=8
for n in range(0,(len(x1)-1)):
    sum=0
    for k in range(0,(len(x1)-1)):
        sum=sum+(x1[n]*np.exp(-j*2*3.14*k*n)/N)
    y1.append(sum)
print(y1)
for n in range(0,(len(x2)-1)):
    sum1=0
    for k in range(0,(len(x2)-1)):
       sum1=sum1+(x2[n]*np.exp(-j*2*3.14*k*n)/N)
    y2.append(sum1)
print(y2)
if(a1*x1[n]+a2*x2[n]==a1*x1[k]+a2*x2[k]):
  print("\nthe linearity property exists.................\n")
else:
  print("\nthe linearity property exists.............\n")
x3=x1+x2
x3[n]=[]
x3[k]=[]
x3[n]=x1[n]+x2[n]
x3[k]=x1[k]+x2[k]
if(x3[n]==x3[k]):
  print("\nthe sum of samples equal to sum of dft samples...........\ni got t\nhulalaaaaaa.........\n")
else:
  print("\nthe sum of samples equal to sum of dft samples...........\ni didn't got it............\n____-----.........\n\n\n")
s1=np.abs(x1[n])
print("magntude of x1[n]",s1)
s2=np.abs(x2[n])
print("magntude of x2[n]",s2)
s3=np.abs(x1[n])
print("magntude of x3[n]",s3)
s4=np.abs(x1[k])
print("magntude of x1[k]",s4)
s5=np.abs(x2[k])
print("magntude of x2[k]",s5)
s6=np.abs(x3[k])
print("magntude of x3[k]",s6)
p1=np.angle(x1[n])
print("\npharse of x1[n]",p1)
p2=np.angle(x2[n])
print("pharse of x2[n]",p2)
p3=np.angle(x3[n])
print("pharse of x3[n]",p3)
p4=np.angle(x1[k])
print("pharse of x1[k]",p4)
p5=np.angle(x2[k])
print("pharse of x2[k]",p5)
p6=np.angle(x3[k])
print("pharse of x3[k]",p6)
print("\nBy MANASA J\n\n")


