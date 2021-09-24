#! /home/heidi/Python/Ensayo

import os

def casa(x,m,w,n,k,y,j,z):
    cs=open("movida.dat", "a")
    cs.write("%d %d %d %d %d %d %d %d\n"%(x,m,w,n,k,y,j,z))
    cs.close()

l=150; c=50; t=0; tf=50; m=120; n=70; k=-110; j=-60
x=-110; w=-110; y=70; z=70

while(t<=tf):
    x+=1
    y+=1
    w+=1
    z+=1
    t+=1
    casa(x,m,w,n,k,y,j,z)
