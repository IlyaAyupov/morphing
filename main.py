import math
import numpy as np
import matplotlib.pyplot as plt
from mpmath import *
fil=open("trans.txt",'r').read().strip().split('\n')
i=0
x=np.zeros((2,1))
x[0][0]=1
x[1][0]=3
dotsX=[]
dotsY=[]
i=len(fil)-4
while i>=0:
    m=np.zeros((2,2))
    a = np.zeros((2,2))
    d = np.zeros((2,2))
    det = float(fil[i].strip().split(' ')[-1])
    i+=1
    trace = float(fil[i].strip().split(' ')[-1])
    i+=1
    m1=fil[i].strip().split('[')[-1][:-1].strip().split(' ')

    m[0][0] = float(m1[0])
    m[1][0] = float(m1[-1])
    i+=1
    m2=fil[i].strip()[1:-2].strip().split(' ')
    m[0][1] = float(m2[0])
    m[1][1] = float(m2[-1])
    i-=7
    d[0][0]=(trace+math.sqrt(trace**2-4*det))/2
    d[1][1]=(trace-math.sqrt(trace**2-4*det))/2
    a=np.dot(np.dot(m,d),np.linalg.inv(m))
    a=np.linalg.inv(a)
    x=np.dot(a,x)
    print(x)
    ff.write('{};{}\n'.format(x[0][0],x[1][0]))
    print(a)
    if 0<x[0][0] and -0.1<x[1][0]<0.2:
        dotsX.append(x[0][0])
        dotsY.append(x[1][0])
print(max(dotsX),max(dotsY))
minX=min(dotsX)
maxX=max(dotsX)
maxY=max(dotsY)
minY=min(dotsY)
mas=np.zeros((int(round(maxY-minY))+1,int(round(maxX-minX))+1))
for i in range(len(dotsX)):
    mas[int(round(dotsY[i]-minY))][int(round(dotsX[i]-minX))]=1
plt.scatter(dotsX,dotsY,s=1)
plt.show()