def Potencia2 (n):
    if n < 2:
        return n
    return 3*Potencia2(n-1)-2*Potencia2(n-2)
