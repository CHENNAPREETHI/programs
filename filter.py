import matplotlib.pyplot as plt
import numpy as np
import math
p= 0.707#input("enter pass band error value:")
s=0.01#input("enter stop band error value:") 
w1=3141.52#input("enter pass band freq:") 
w2= 6283.4#input("enter stop band freq:")
a=(p*p)
p=1/a
x=p-1

b=s*s
q=1/b
y=q-1
k=0.5*np.log(x/y)
l=np.log(w1/w2)
r=np.around(k/l)
s=np.abs(r)
print(s)
c=1/(2*s)
w3=(w1/(x**c))
print(w3)
H=np.zeros(10000)
for i in range(0,10000):
	d=(i/w3)**(2*s)
	e=np.sqrt(1+d)
	H[i]=1/e
Hmag=np.abs(H)
print(H)
plt.subplot(121)
plt.plot(Hmag)
plt.show()
