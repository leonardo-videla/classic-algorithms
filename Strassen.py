import math

def  Strassen(A, B):

    n=len(A)

    if n==1:
        return [ [ A[0][0]*B[0][0] ] ]

    m=math.floor(n/2)

    A11=[[A[i][j] for j in range(m)] for i in range(m)]
    A12=[[A[i][j] for j in range(m,n)] for i in range(m)]
    A21=[[A[i][j] for j in range(m)] for i in range(m,n)]
    A22=[[A[i][j] for j in range(m,n)] for i in range(m,n)]

    B11=[[B[i][j] for j in range(m)] for i in range(m)]
    B12=[[B[i][j] for j in range(m,n)] for i in range(m)]
    B21=[[B[i][j] for j in range(m)] for i in range(m,n)]
    B22=[[B[i][j] for j in range(m,n)] for i in range(m,n)]

    M1 = Strassen (Suma (A11, A22), Suma (B11, B22))
    M2 = Strassen (Suma (A21, A22), B11)
    M3 = Strassen (A11, Suma (B12, Inverso(B22)))
    M4 = Strassen (A22, Suma (B21, Inverso(B11)))
    M5 = Strassen (Suma (A11, A12), B22)
    M6 = Strassen (Suma (A21, Inverso(A11)), Suma (B11, B12))
    M7 = Strassen (Suma (A12, Inverso (A22)), Suma (B21, B22))

    C11= Suma (Suma(Suma(M1, M4), M7), Inverso(M5))
    C12= Suma(M3, M5)
    C21= Suma (M2, M4)
    C22 = Suma ( Suma (Suma (M1, M3), M6), Inverso (M2))


    C=[]
    for k in range(m):
        C.append(C11[k]+C12[k])
    for k in range(m):
        C.append(C21[k]+C22[k])

    return C
    

def Suma (m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range (len(m1))] for i in range (len(m1))]

def Inverso (m):
    return [[-1*m [i][j]  for j in range (len(m)) ] for i in range (len (m))]
