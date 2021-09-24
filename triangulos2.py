#! /home/heidi/Python/Parcial

import numpy as np
import os
from math import fabs
from pylab import matplotlib as plt

pts=open("mmm.dat", "w")
#scr=open("script_triangulo.gpl", "w")

def triangulo(n):
    while (n!=0) and (n>0): 
        n-=1
        L=100.0
        H=np.sqrt(3)*L/2 
        if n==0: 
            pts.write("%d\t%d\n%d\t%d\n%.1f\t%.1f\n"%(0,0,L,0,L/2,H)) 
          #  scr.write("set terminal png\n")
           # scr.write("set output 'base.png'\n")
            #scr.write("plot [0:100][0:100] 'mmm.dat' u 1:2 lw 3 w lines\n")
        else: 
            m=3**(n-1)
            j=1 
            q=0 
            while j<=m: 
                l=L/(2**n)
                h=H/(2**n) 
                r=3**j
                s=0
                p=0
                w=0
                z=0
                while p < m: 
                    q=q
                    print w 
                    d=l+ w 
                    e=l/2 + w 
                    f=3*l/2 + w 
                    g=q*h 
                    k=(q+1)*h 
                    i=0 
                    p+=1 
                    z+=1 
                    if p!=0: 
                        t=p%3 
                        if t==0:
                            print d, e , f 
                            d1=2*d/5 
                            e1=e/3 
                            f1=5*e1/3 
                            g=2*h 
                            k=3*h 
                            for i in range(1):
                                a1=d1 
                                a2=g 
                                b1=e1 
                                b2=k 
                                c1=f1 
                                c2=b2 
                                pts.write("%.1f\t%.1f\t%d\n%.1f\t%.1f\t%d\n%.1f\t%.1f\t%d\n"%(a1,a2,00,b1,b2,00,c1,c2,00))
                        else:
                            for i in range(1):
                                a1=d 
                                a2=g
                                b1=e 
                                b2=k 
                                c1=f 
                                c2=b2
                                pts.write("%.1f\t%.1f\t%d\n%.1f\t%.1f\t%d\n%.1f\t%.1f\t%d\n"%(a1,a2,s,b1,b2,j,c1,c2,p))
                        if (p>=3) and (p<6): 
                            z=3/2 
                        if(p>=6) and (p<9):
                            z=5/2 
                        s+=1 
                        j+=1 
                        w=2*l*z

n=4 
triangulo(n)
pts.close()
#scr.close()
#os.system("gnuplot script_triangulo.gpl")

