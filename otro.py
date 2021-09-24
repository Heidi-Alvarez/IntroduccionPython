#! /home/heidi/Python/Ensayo

import numpy as np
import os

def grafica(t, x, y):
    pos=open("posicion.dat", "w")
    scr=open("script_ensayo.gpl", "w")
    pos.write("%d %f %f"%(t,x,y))
    pos.close()
    scr.write("set terminal png\n")
    scr.write("set output 'ensayo%4.d.png'\n"%t)
    scr.write("plot [-150:150][-150:150]'./posicion.dat' u 2:3 lt 0.5 w circles title 'Ebrio', './extremos.dat' u 1:2 lt 2 t '', './extremos.dat' u 3:4 lt 2 t '', './extremos.dat' u 5:6 lt 2 t '', './extremos.dat' u 7:8 lt 2 t '', './casa.dat' u 1:2 lt 3 t '', './casa.dat' u 3:4 lt 3 t '', './casa.dat' u 5:6 lt 3t '', './casa.dat' u 7:8 lt 3 t ''\n")
    scr.close()
    os.system("gnuplot script_ensayo.gpl")

l=150.0; x=0.0; y=0.0; t=0; p=5.5; c=50.0

while(x>=-l and x<=l and y>=-l and y<=l):
    beta=2*np.pi*np.random.rand()
    x+=p*np.cos(beta)
    y+=p*np.sin(beta)
    t+=1
    grafica(t,x,y)
    if(x>=l-c and y<=c-l):
        print #at home!
        break
    if(x<-l):
        x=l
    if(x>l):
        x=-l
    if(y<-l):
        y=l
    if(y>l):
        y=-l

os.system("convert *.png Heidi_Alvarez.gif")
os.system("rm *.png")
