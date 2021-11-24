import math
import random
import sys
import time

def QS (x, inicio, final):
    if (final-inicio)<1:
        return
    p=random.random()
    m=inicio+math.floor(p*(final-inicio+1))   #Aquí se puede eliger el pivote de otro modo
    aux=x[inicio]
    x[inicio]=x[m]
    x[m]=aux
    pos=Particiona2 (x, inicio, final)
    QS (x, inicio, pos-1)
    QS (x, pos+1, final)
    return

def Particiona (x, inicio, final, pivote):
    menores=[]
    mayores=[]
    i=0

    for k in range (inicio, final+1):
        if (x[k]<pivote):
            menores.append(x[k])
            i=i+1
        if (x[k]> pivote):
            mayores.append(x[k])

    n1=len(menores)
    n2=len(mayores)
    j=0
    for k in range(n1):
        x[inicio+j]=menores[k]
        j=j+1
    x[inicio+j]=pivote
    pos=inicio+j
    j=j+1
    for k in range(n2):
        x[inicio+j]=mayores[k]
        j=j+1
    return pos

def Particiona2 (x, inicio, final):
    i=inicio+1
    p=x[inicio]
    for j in range(inicio+1, final+1):
        if x[j]<p:
            aux=x[i]
            x[i]=x[j]
            x[j]=aux
            i=i+1
    aux=x[inicio]
    x[inicio]=x[i-1]
    x[i-1]=aux
    return (i-1)

#As main
if __name__=="__main__":
    str = sys.argv[1].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
    x=[int(i) for i in str]
    print("La lista original es: ", x)
    QS(x, 0, len(x)-1)
    print("La lista ordenada por QS es: ",x)
