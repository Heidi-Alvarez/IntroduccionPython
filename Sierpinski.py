#! /home/heidi/Python/Parcial

import numpy as np
import os
from math import fabs
from pylab import matplotlib as plt

pos=open("puntos.dat", "w")

L=200
x1=0
x2=0
y1=L
y2=0
z1=L/2
z2=np.sqrt(3)*L/2
a=0
i=0
def triangulo(n):
    while(n!=0):
        n-=1
        if n==0:
            pos.write("%.1f\t%.1f\t%d\t%.1f\n"%(x1,x2,n,0))
            pos.write("%.1f\t%.1f\t%d\t%.1f\n"%(y1,y2,n,0))
            pos.write("%.1f\t%.1f\t%d\t%.1f\n"%(z1,z2,n,0))
        else:
            m=3*n
            print n
            a=L/(2**n)
            b=a/4.0
            c=a/2.0
            print a
            print b
            print c
            print m
            for j in range(m):
                a=L*(2*j+1)/(2**(n))
                b=a*(2*j+1)/4.0
                c=a*(2*j+1)/2.0
                d=a*j
                e=a
                print a
                print b
                print c
                print m
                for i in range(1):
                    w1=(fabs(y1-x1))/(2**n)+ d*(i+1) 
                    w2=(np.sqrt(3)*L/(4**n))*2*j 
                    u1=(fabs(y1-z1))/(2**n) + d*(i+1)
                    u2=(fabs(y2-z2))/(2**n) 
                    v1=(fabs(z1-x1))/(2**(n))+ e
                    v2=(fabs(z2-x1))/(2**n)+(n-1)*b*j 
                    pos.write("%.1f\t%.1f\t%d\t%.1f\n"%(w1,w2,i,a))
                    pos.write("%.1f\t%.1f\t%d\t%.1f\n"%(u1,u2,n,b))
                    pos.write("%.1f\t%.1f\t%d\t%.1f\n"%(v1,v2,n,c))
                    
                    
n=4
triangulo(n)


pos.close()
