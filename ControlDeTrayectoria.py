# encoding: utf-8
import numpy
import math

L1 = 100.0
L2 = 50.0

def cosq2(x,y):
    return (pow(x,2) + pow(y,2) - pow(L1,2) - pow(L2,2))/(2*L1*L2)
def addResult(q1,q2,x,y):
    return [q1,q2,x,y]
###
#Posiciones iniciales
x = 100
yInicial = 100

yFinal = 50 #Posición en Y donde llega el brazo
step = 10   #Cada cuánta distancia hay un punto de muestreo
resultado = []
for y in reversed(range(yFinal,yInicial,10)):
    print("y = "+str(y))
    aux = []
    q1 = numpy.arctan(x/y)
    cosQ2 = ((pow(x,2) + pow(y,2) - pow(L1,2) - pow(L2,2))/(2*L1*L2))#cosq2(x,y)
    if(cosQ2 == 0):
        #error ; añadir a errores
        q2 = float('Inf')
    else:
        q2 = numpy.arctan(math.sqrt(1-pow(cosQ2,2)))/(cosQ2)
    
    aux.append(q1)
    aux.append(q2)
    aux.append(x)
    aux.append(y)
    resultado.append(aux)

print("q1\tq2\tx y")
for res in resultado:
    print(str(res))


