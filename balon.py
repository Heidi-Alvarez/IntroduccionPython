#! home/heidi/Python/Tarea.1

import os

def datos(ty, tx, x, y):
    pos=open("posicion.dat", "a")
    pos.write("%.2f %.2f %.2f %.2f\n"%(ty,tx,x,y))
    pos.close()

def grafica(ty, tx, x, y):
    pos=open("posicion.dat", "a")
    scr=open("script_balon.gpl", "w")
    pos.write("%.2f %.2f %.2f %.2f\n"%(ty,tx,x,y))
    pos.close()
    scr.write("set grid \n")
    scr.write("set title 'REBOTES %.3f seg'\n" %ty)
    scr.write("set xlabel 'Distancia (m)'\n")
    scr.write("set ylabel 'Altura (m)'\n")
    scr.write("set terminal png\n")
    scr.write("set output 'balon%4.d.png'\n"%(tx))
    scr.write("plot [0:10000][0:350] './posicion.dat' u 3:4 lt 5 lw 3 w lines\n")
    scr.write("reset\n")
    scr.close()
    os.system("gnuplot script_balon.gpl")

h=200; voy=50; vox=55.0; ty=0.0; tx=0.0; g=9.8; y=0.0; x=0.0; vy=voy

while (tx<=170):
    tx+=0.1
    ty+=0.1
    y=h+voy*ty-0.5*g*ty*ty
    x=vox*tx
    vy=voy-g*ty
    grafica(ty, tx, x, y)
    if y<=0:
        voy=-vy*0.9
        h=0.0
        ty=0.0

os.system("convert *.png balon.gif")
os.system("rm *.png")


