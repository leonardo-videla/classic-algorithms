import math
import sys
import time

def Simple_Sort (x):
    n=len(x)
    y=x;
    for i in range(1,n):
        for j in range (i):
            if (y[i]<y[j]):
                aux=y[i]
                for k in range (i-1, j-1, -1):
                    y[k+1]=y[k]
                y[j]=aux
    return y

#As main
if __name__=="__main__":
    str = sys.argv[1].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
    x=[int(i) for i in str]
    print("La lista original es: ", x)
    start=time.time()
    print("La lista ordenada por InsertionSort es: ", Simple_Sort(x))
    print("Tiempo de ejecucion: ", time.time()-start)
