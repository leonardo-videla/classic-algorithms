import math

def  Secuencias (n):


    if n==2:
        return [[0,0], [1,0], [0,1]]
    if n > 2:
        lista=Secuencias (n-1)
        nueva_lista=[]
        for sec in lista:
            nueva_lista.append(sec+[0])
            if (sec[len(sec)-1]==0):
                nueva_lista.append(sec+[1])
        return nueva_lista
