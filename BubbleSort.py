import math
import sys
import time

def BubbleSort (x):
    n=len(x)
    y=x;
    swap=0
    for i in range(n-1):
        if (y[i+1]<y[i]):
            aux=y[i+1]
            y[i+1]=y[i]
            y[i]=aux
            swap=1
    m=n-1
    while swap and m>0:
        swap=0
        for i in range(m-1):
            if (y[i+1]<y[i]):
                aux=y[i+1]
                y[i+1]=y[i]
                y[i]=aux
                swap=1
        m=m-1
    return y

#As main
if __name__=="__main__":
    str = sys.argv[1].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
    x=[int(i) for i in str]
    print("La lista original es: ", x)
    start=time.time()
    print("La lista ordenada por BubbleSort es: ", BubbleSort(x))
    print("Tiempo de ejecucion: ", time.time()-start)
