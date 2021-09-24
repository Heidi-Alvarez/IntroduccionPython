#! /home/heidi/Python/Tarea.1

import numpy

e=1.0; fac=1.0

#n=raw_input("Ingrese el numero hasta el cual desea llegue la serie\n")
j=1.0

for i in range(500):
    j+=1
    fac*=j
    e+=1/fac

print "e=%.50lf"%e


    
