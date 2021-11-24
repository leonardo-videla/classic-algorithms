import math

def  Hanoi (n, i, j):

    k=6-i-j
    if n==1:
        print ("MOVER DISCO DESDE POSTE ", i, " HACIA POSTE ", j)
        return
    if n> 1:
        Hanoi (n-1, i, k)
        Hanoi (1, i,j)
        Hanoi (n-1, k, j)
