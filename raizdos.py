#! /home/heidi/Python/Tarea.1

import numpy

r=1.0; n=0.0

for n in range(500):
    fcu=1.0/(4*n+1)
    tu=1+fcu
    fcd=1.0/(4*n+3)
    td=1-fcd
    r*=tu*td

print "%.52lf" %r




