# encoding: utf-8
import numpy
import math
import matplotlib.pyplot as plt

L1 = 100.0
L2 = 50.0

y = 100.0
xInicial = 101

xFinal = 50 # Posición en X donde llega el brazo
Q1 = []
Q2 = []
tiempo = 0.0
Tiempo = []
for x in reversed(range(xFinal,xInicial,1)):

    # https://roboted.wordpress.com/fundamentals/
    cosq2 = (x**2+y**2-L1**2-L2**2) / (2*L1*L2)
    numerator = (x**2+y**2+L1**2-L2**2)
    denominator = 2*L1*math.sqrt((x**2+y**2))
    q1 = math.atan(y/x) - math.acos(numerator/denominator)
    q2 = math.atan2(math.sqrt(1-math.pow(cosq2,2)), cosq2)
    Q1.append(q1)
    Q2.append(q2)
    Tiempo.append(tiempo)
    tiempo+=2.0/50.0

plt.figure()
plt.plot(Tiempo, Q1)
plt.ylabel('Q1')
plt.xlabel('Tiempo (s)')
plt.figure()
plt.plot(Tiempo, Q2)
plt.ylabel('Q2')
plt.xlabel('Tiempo (s)')
plt.show()

