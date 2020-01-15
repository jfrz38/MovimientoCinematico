import math
import matplotlib.pyplot as plt

class Kine2:
    def cosq2(self, angulo):
        positiveResult = math.atan2(math.sqrt(1-math.pow(angulo,2)), angulo)
        #negativeResult = math.atan2(math.sqrt(1-math.pow(angulo,2))*(-1), angulo)
        return (positiveResult)
    def inputCalc(self):
        x = 50.0
        y = 100.0
        L1 = 100
        L2 = 50
        auxTiempo = []
        tiempo=0.0
        Q1 = []
        Q2 = []
        #Recorrer paso a paso desde x = 100 hasta x = 50
        for x in reversed(range(50,100,1)):
            cosQ2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
            stheta2 = math.sqrt(1-math.pow(cosQ2, 2))
            ctheta1 = (x * (L1 + L2 * cosQ2) + y * L2 * stheta2) / (x**2 + y**2)
            q1 = self.cosq2(ctheta1)
            q2 = self.cosq2(cosQ2)
            #print("q1 = "+str(q1)+" ; q2 = "+str(q2))
            Q1.append(q1)
            Q2.append(q2)
            auxTiempo.append(tiempo)
            #Cada movimiento se realiza en un instante de tiempo
            #En total 50 movimientos en 2 segundos
            tiempo += 2.0/50.0
        plt.figure()
        plt.plot(auxTiempo, Q1)
        plt.ylabel('Q1')
        plt.figure()
        plt.plot(auxTiempo, Q2)
        plt.ylabel('Q2')
        plt.show()
kine2 = Kine2()
kine2.inputCalc()
