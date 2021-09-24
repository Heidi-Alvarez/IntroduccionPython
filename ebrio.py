#! /home/heidi/Python/Tarea.2

import numpy as np
import os

def graf(t,x,y):
    pos=open("posicion_XD.dat", "a")
    scr=open("script_ebrio.gpl", "w")
    pos.write("%f %f %f\n"%(t,x,y))
    pos.close()
    scr.write("set terminal png\n")
    scr.write("set output 'ebrio%4.f.png'\n"%t)
    scr.write("set size square\n")
    scr.write("set xrange[-200:200]\n")
    scr.write("set yrange[-200:200]\n")
    scr.write("plot (x**2)/7 lw 1.2 lt 4 w impulses t'', -(x**2)/7 lw 1.2 lt 4 w impulses t '', (x**3)/60000 lw 1.5 lt 5 w impulses t'', -(x**3)/60000 lw 1.5 lt 5 w impulses t'', './lados.dat' u 1:2 lt 6 lw 5 t'', './lados.dat' u 3:4 lt 6 lw 5 t'', './base_techo.dat' u 1:2 lt 6 lw 5 t'', './base_techo.dat' u 3:4 lt 6 lw 5 t'', './paredes.dat' u 1:2 lt 3 lw 3 t'', './paredes.dat' u 3:4 lt 3 lw 3 t'','./casa.dat' u 1:2 lt 3 lw 3 t'', './casa.dat' u 3:4 lt 3 lw 3 t'', './techo.dat' u 1:2 lt 3 lw 3 t'', './techo.dat' u 3:4 lt 3 lw 3 t'', './posicion_dos.dat' u 2:3 lw 0.1 lt 1  w circles t''\n")
    scr.close()
    os.system("gnuplot script_ebrio.gpl")

x=0.0; y=0.0; l=75.0; t=0.0; c=25.0

while (x>=-l and x<=l and y>=-l and y<=l):
    alpha=2.0*np.pi*np.random.rand()
    x+=5*np.cos(alpha)
    y+=5*np.sin(alpha)
    t=t+1
    graf(t,x,y)
    if(x<-l):
        x=l
    if(x>l):
        x=-l
    if(y<-l):
        y=l
    if(y>l):
        y=-l
    if((x>=(l-c)) and (y<=(c-l))):
        print "#at home!"
        break

os.system("convert *.png HeidiAlvareztresXD.gif")
os.system("rm *.png")

        
