import math
import sys
import time

def Merge (izq, der):
    n1=len(izq)
    n2=len(der)

    y=[]
    i=0
    j=0
    while i < n1 and j < n2:
        if (izq[i]<der [j]):
            y.append(izq[i])
            i=i+1
        else:
            y.append(der[j])
            j=j+1

    if i==n1:
        for k in range (j, n2):
            y.append(der[k])
    if j==n2:
        for k in range (i, n1):
            y.append(izq[k])
    return y

def Merge_Sort (x):
    n=len(x)
    if n==1:
        return x
    m=math.floor(n/2)
    izq=Merge_Sort (x[:m])
    der=Merge_Sort (x[m:])
    return Merge(izq, der)

#As main
if __name__=="__main__":
    str = sys.argv[1].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
    x=[int(i) for i in str]
    print("La lista original es: ", x)
    start=time.time()
    print("La lista ordenada por MergeSort es: ", Merge_Sort(x))
    print("Tiempo de ejecucion: ", time.time()-start)
