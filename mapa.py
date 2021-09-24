#! /home/heidi/Python/Logistico
# -*- coding: utf-8 -*-

import numpy as np
import os

def base(n):
    if n==1:
        dato=z
    elif n>1:
        dato=r*base(n-1)*(1-base(n-1))
    return dato

def grafica(i,r,x):
    p=int(r)+1
    dt=open("mapa%d.dat"%(i), "r")
    scr=open("script_mapa.dat", "w")
    scr.write("set terminal png\n")
    scr.write("set xlabel 'Repeticiones' \n")
    scr.write("set ylabel 'Poblacion' \n")
    scr.write("set output '%dmapa%d.png'\n"%(c,i))
    scr.write("set title 'x=%.3f' \n"%(x))
    scr.write("plot './mapa%d.dat' lt %d t 'r=%.2f' w lines \n"%(i,p,r))
    scr.close()
    os.system("gnuplot script_mapa.dat")

c=0

for c in range(4):
    if c==0:
        a=1
    if c==1:
        a=0.5
    if c==2:
        a=1.5
    if c==3:
        a=0.79
    if c==4:
        a=0.85*np.random.randint(7)

    n=0; m=20; j=5; r=0; i=0
    
    for i in range (j):
        r+=a
        i+=1
        for n in range (m):
            n+=1
            x=0.79
            z=r*x*(1-x)
            dt=open("mapa%d.dat"%(i), "a")
            datos=base(n)
            dt.write("%d \t %f\n"%(n,datos))
            grafica(i,r,x)
            dt.close()

    dt.close()
    
    k=c
    os.system("convert *.png Mapa%d.gif"%c)
    os.system("convert %dmapa1.png %dmapa1.jpl"%(c,k))
    os.system("convert %dmapa2.png %dmapa2.jpl"%(c,k))
    os.system("convert %dmapa3.png %dmapa3.jpl"%(c,k))
    os.system("convert %dmapa4.png %dmapa4.jpl"%(c,k))
    os.system("convert %dmapa5.png %dmapa5.jpl"%(c,k))
    os.system("rm *.png")
    os.system("rm *dat")


