#! /home/heidi/Python/Tarea.2

import math as math
import numpy as np
import os

lado=open("lados.dat", "w")

l=200.0; y=-200.0; z=-200.0

while(y<=l and y>=-l and z<=l and z>=-l):
    x=-200.0
    y+=0.1
    w=200.0
    z+=0.1
    lado.write("%f %f %f %f\n"%(x, y, w, z))

lado.close()

byt=open("base_techo.dat", "w")

l=200.0; x=-200.0; w=-200.0

while(x<=l and x>=-l and w<=l and w>=-l):
    y=-200.0
    x+=0.1
    z=200.0
    w+=0.1
    byt.write("%f %f %f %f\n"%(x, y, w, z))
byt.close()

paredes=open("paredes.dat", "w")

l=200.0; c=75.0; y=-l; z=-l

while(y<=c-l and y>=-l and z<=c-l and z>=-l):
    x=l-c
    y+=0.1
    w=l
    z+=0.1
    paredes.write("%f %f %f %f\n"%(x,y,w,z))
paredes.close()

casa=open("casa.dat", "w")

l=200.0; c=75.0; x=l-c; w=l-c

while(x>=l-c and x<=l and w>=l-c and w<=l):
    y=-l
    x+=0.1
    z=c-l
    w+=0.1
    casa.write("%f %f %f %f\n"%(x,y,w,z))
casa.close()

techo=open("techo.dat", "w")

l=200.0; c=75.0; x=l-c; w=l; y=c-l; z=c-l

while(x>=l-c and x<=l-(c/2) and w>=l-(c/2) and w<=l):
    x+=0.1
    y+=0.1
    w-=0.1
    z+=0.1
    techo.write("%f %f %f %f\n"%(x,y,w,z))
techo.close()

