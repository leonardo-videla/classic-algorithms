import math

def  Hamiltonian (q,n):

# Retorna las q^n secuencias en el alfabeto {1,2,...,q} en un orden tal que
# dos consecutivas difieren solo en una letra.

    if n==1:
        lista=[]
        for j in range(1, q+1):
            lista.append([j])
        return lista
    if n > 1:
        l1=Hamiltonian (q, n-1)
        l2=Invierte_Lista(l1)
        nueva_lista=[]
        flag=1

        for j in range(1, q+1):
            aux=[]
            if flag==1:
                aux=l1
            else:
                aux=l2
            flag=-1*flag
            for sec in aux:
                nueva_lista.append(sec+[j])
        return nueva_lista

def Invierte_Lista (l):
    aux=[]
    n=len(l)
    for i in range (n):
        aux.append(l[n-1-i])
    return aux
