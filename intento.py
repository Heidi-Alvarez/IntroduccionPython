#! /home/heidi/Python/Parcial

import numpy as np
from math import fabs
import os

n=10; L=100.0; H=np.sqrt(3)*L/2; j=0; i=0

while j <= n:
    if j==0:
        pts=open("iteraciones%.3d.dat"%j, "w")
        pts.write("%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f"%(0,0,L,0,(L/2),H))
        pts.close()
    pts=open("iteraciones%.3d.dat"%j, "r")
    puntos=pts.readlines()
    for punto in puntos:
        x1=float(punto.split("\t")[0]) 
        x2=float(punto.split("\t")[1])
        y1=float(punto.split("\t")[2]) 
        y2=float(punto.split("\t")[3])
        z1=float(punto.split("\t")[4]) 
        z2=float(punto.split("\t")[5])
        print x1,x2,y1,y2,z1,z2
        print "=D"
        ax=x1
        ay=x2
        dx=fabs(y1-x1)/2
        dy=ay
        fx=fabs(dx-ax)/2
        fy=z2/2
        bx=y1
        by=y2
        ex=fx + dx
        ey=fy
        cx=z1
        cy=z2
        print x1,x2,y1,y2,z1,z2
        print "XD"
        print ax,ay,dx,dy,fx,fy
        print dx,dy,bx,by,ex,ey
        print fx,fy,cx,cy,ex,ey
        pos=open("iteraciones%.3d.dat"%(i+1), "w")
        pos.write("%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f"%(ax,ay,dx,dy,fx,fy))
        pos=open("iteraciones%.3d.dat"%(i+2), "w")
        pos.write("%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f"%(dx,dy,bx,by,ex,ey))
        pos=open("iteraciones%.3d.dat"%(i+3), "w")
        pos.write("%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f"%(fx,fy,cx,cy,ex,ey))
        i=3*(j+1)
    j+=1

i=i

pts.close()
pos.close()

def grafica(t):
    scr=open("script_Sierpinski%.3d.dat"%t, "w")
    scr.write("set terminal png \n")
    scr.write("set output 'triangulo%.3d.png'\n"%t)
    scr.write("plot [0:100][0:100] './iteraciones%.3d.dat' u 1:2 lw 5 lt 1 w circles, './iteraciones%.3d.dat' u 3:4 lw 5 lt 1 w circles, './iteraciones%.3d.dat' u 5:6 lw 5 lt 1 w circles \n"%(t,t,t))
    scr.close()
    os.system("gnuplot script_Sierpinski%.3d.dat"%t)

t=0
p=i-2

for t in range (p):
    t+=1
    grafica(t)

