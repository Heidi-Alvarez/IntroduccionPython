#! /home/heidi/Python/Parcial

import numpy as np 
pts=open("triangulos.dat", "w") 

def triangulo(n):
    while (n!=0) and (n>0): 
        n-=1
        L=100.0
        H=np.sqrt(3)*L/2 
        if n==0: 
            pts.write("%d\t%d\n%d\t%d\n%.1f\t%.1f\n"%(0,0,L,0,L/2,H)) 
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
                    #print w 
                    d=l+ w 
                    e=l/2 + w 
                    f=3*l/2 + w 
                    g=q*h 
                    k=(q+1)*h 
                    i=0 
                    p+=1 
                    z=1+z 
                    w=2*l*z
                    print p, z
                    if p!=0: 
                        t=p%3 
                        if t==0:
                            #print d, e , f 
                            d1=2*p*d/15     #2*d/5 
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
                        if p==3: 
                            print z
                            z=2.0 
                            print z
                        if p==6:
                            z=5/2.0 
                            print z
                        if p==9:
                            z=7/2.0
                            print z
                        if p==12:
                            z=9/2.0
                        if p==15:
                            z=11/2.0
                        if p==18:
                            z=13/2.0
                        s+=1 
                        j+=1 
                        z=z
                        #print z
                        w=2*l*z

n=3
triangulo(n)
pts.close()


















