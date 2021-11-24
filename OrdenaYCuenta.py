import math
import sys
import time

def MezclaYCuenta (izq, der):
    n1=len(izq)
    n2=len(der)

    y=[]
    i=0
    j=0
    count=0
    while i < n1 and j < n2:
        if (izq[i]<=der [j]):
            y.append(izq[i])
            i=i+1
        else:
            count=count+n1-i
            y.append(der[j])
            j=j+1

    if i==n1:
        for k in range (j, n2):
            y.append(der[k])
    if j==n2:
        for k in range (i, n1):
            y.append(izq[k])
    return y, count

def OrdenaYCuenta (x):
    n=len(x)
    if n==1:
        return [x, 0]
    m=math.floor(n/2)
    izq, i1=OrdenaYCuenta (x[:m])
    der,i2=OrdenaYCuenta (x[m:])
    m, i3=MezclaYCuenta (izq, der)
    return m, (i1+i2+i3)

#As main
if __name__=="__main__":
    str = sys.argv[1].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
    x=[int(i) for i in str]
    print("La lista original es: ", x)
    start=time.time()
    m,c=OrdenaYCuenta(x)
    print("La lista ordenada por MergeSort es: ", m)
    print("La lista original tenia ", c, " inversiones.")
    print("Tiempo de ejecucion: ", time.time()-start)
