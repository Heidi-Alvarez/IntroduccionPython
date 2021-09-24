#! /home/heidi/Python/Logistico


import numpy as np
from math import fabs
import os

i=0; n=21; a=1.; b=1./np.sqrt(2); p=1.; t=0.25; den=0; num=0; pi=0

dt=open("pi.dat", "w")

def grafica():
    sct=open("script_pi.png", "w")
    sct.write("set terminal png \n")
    sct.write("set title 'Calculo de Pi' \n")
    sct.write("set output 'Metodo de Gauss Legendre' \n")
    sct.write("plot [0:20][2.5:4] pi, './pi.dat' u 1:2 t 'Pi.Gauss-Legendre ' w lines \n")
    sct.close()
    os.system("gnuplot script_pi.png")

for i in range(n):
    print a, b, p, t
    num=(a+b)**2
    den=4.*t
    print num, den
    pi=num/den
    print pi
    error=fabs(np.pi-pi)
    dt.write("%d\t%.40lf\t%.40lf\n"%(i, pi, error))
    c=a
    e=b
    a=(c+e)/2.
    b=np.sqrt(c*e)
    p=2.*p
    d=a-c
    f=p*d**2.
    t=t-f

dt.close()

grafica=grafica()

