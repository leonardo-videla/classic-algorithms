import math
import sys
import time

def QuickSort (x):
    n=len(x)

    if n<=1:
        return x


    m=n-1
    pivote=x[m]
    menores=[]
    mayores=[]
    i=0

    if n >= 2:
        for z in x:
            if (z<=pivote and i!=m):
                menores.append(z)
            if (z>pivote):
                mayores.append(z)
            i=i+1
    y=[]

    if (len(menores)>0):
        a=QuickSort(menores)
        y.extend(a)
    y.append(pivote)
    if (len(mayores)>0):
        b=QuickSort(mayores)
        y.extend(b)
    return y

#As main
if __name__=="__main__":
    str = sys.argv[1].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
    x=[int(i) for i in str]
    print("La lista original es: ", x)
    start=time.time()
    print("La lista ordenada por QuickSort es: ", QuickSort(x))
    print("Tiempo de ejecucion: ", time.time()-start)
