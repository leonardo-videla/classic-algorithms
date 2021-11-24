import math

def Fib2 (n):
    if n<=1:
        return 1
    else:
        x0=1
        x1=1
        r=x1+x0
        if n>2:
            for j in range (2, n):
                x0=x1
                x1=r
                r=x0+x1
        return r
