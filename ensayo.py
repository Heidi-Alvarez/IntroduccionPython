#! /home/heidi/Python/Tarea.1

from pylab import *
plt=matplotlib.pyplot
import numpy
import math
def CARBONO14(No):

    TM=5730;
    Nt=No/100;
    t=TM*math.log(No/Nt)
    return t

def URANIO235(No):
    TM=7e8
    Nt=No/100
    t=TM*math.log(No/Nt)
    return t

def NEUTRON(No):
    TM=885.7/3600
    Nt=No/100
    t=TM*math.log(No/Nt)
    return t

def CALCIO41(No):
    TM=1.03e5
    Nt=No/100
    t=TM*math.log(No/Nt)
    return t

def DECAIMIENTO(No):
    C14=CARBONO14(No)
    U235=URANIO235(No)
    N=NEUTRON(No)
    C41=CALCIO41(No)
    print ("\n\nEl tiempo de decaimiento para que los elementos lleguen al uno por ciento de su cantidad incial es\n\n\tELEMENTO\tTIEMPO\n\n\tCarbono 14\t%f\n\tUranio 235\t%f\n\tNeutron\t\t%f\n\tCalcio 41\t%f\n" %(C14, U235, N, C41))

def GCARBONO14(No, ti, M):
    TM=5730.0
    t=ti
    Nt=M*math.exp(-t/TM)
    return(Nt)

def GURANIO235(No, ti, M):
    TM=7e8
    t=ti
    Nt=M*math.exp(-t/TM)
    return(Nt)

def GNEUTRON(No, ti, M):
    TM=885.7/3600
    t=ti
    Nt=M*math.exp(-t/TM)
    return(Nt)

def GCALCIO41(No, ti, M):
    TM=1.03e5
    t=ti
    Nt=M*math.exp(-t/TM)
    return (Nt)

def DECAIMIENTOG(No, ti, M):
    GC14=GCARBONO14(No, ti, M)
    GU235=GURANIO235(No, ti, M)
    GN=GNEUTRON(No, ti, M)
    GC41=GCALCIO41(No, ti, M)
    print "%f %f %f %f %f"%(ti, GC14, GU235, GN, GC41)


No=100.0
M=100.0
ti=0.0
deca=DECAIMIENTO(No)


calcio=open("ecalcio.dat", "a")
uranio=open("euranio.dat", "a")
neutron=open("eneutron.dat", "a")
carbono=open("ecarbono.dat", "a")

k=1.113

while ti<=k:
    ti+=0.01113
    cbn=GCARBONO14(No, ti, M)
    carbono.write("%f %f\n"%(ti, cbn))
    un=GURANIO235(No, ti, M)
    uranio.write("%f %f\n"%(ti, un))
    nt=GNEUTRON(No, ti, M)
    neutron.write("%f %f\n"%(ti, nt))
    cl=GCALCIO41(No, ti, M)
    calcio.write("%f %f\n"%(ti, cl))

k=26387.625

while ti<=k:
    ti+=263.865
    cbn=GCARBONO14(No, ti, M)
    carbono.write("%f %f\n"%(ti, cbn))
    un=GURANIO235(No, ti, M)
    uranio.write("%f %f\n"%(ti, un))
    cl=GCALCIO41(No, ti, M)
    calcio.write("%f %f\n"%(ti, cl))

k=474332.531

while ti<=k:
    ti+=4479.449
    un=GURANIO235(No, ti, M)
    uranio.write("%f %f\n"%(ti, un))
    cl=GCALCIO41(No, ti, M)
    calcio.write("%f %f\n"%(ti, cl))

k=3223619072.0

while ti<=k:
    ti+=32231447.39
    un=GURANIO235(No, ti, M)
    uranio.write("%f %f\n"%(ti, un))
    
carbono.close()
uranio.close()
neutron.close()
calcio.close()

calcio=open("ecalcio.dat", "r")
uranio=open("euranio.dat", "r")
neutron=open("eneutron.dat", "r")
carbono=open("ecarbono.dat", "r")


x=linspace(0,10000000000,500)
linea1=plt.plot(x,carbono)
linea2=plt.plot(x,uranio)
linea3=plt.plot(x,neutron)
linea4=plt.plot(x,calcio)







