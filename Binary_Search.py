import math

def  Binary_Search (data, key):
    ar=[]
    l=len(data)
    for i in range (l):
            ar.append ([data[i], i])
    return Busca (ar, key)

def Busca (ar, key):
    l=len(ar)
    if (l==1):
        if (ar[0][0] == key):
            return ar[0][1]
        else:
            return -1
        
    m=math.floor(l/2)
   
    if (ar[m][0] > key):
        return Busca ([x for x in ar[:m] ], key )
    else:
        return Busca ([x for x in ar[m:]  ],key )
