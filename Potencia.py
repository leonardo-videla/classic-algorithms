import math

def  Potencia (base, exponente):
    if exponente==1:
        return base
    else:
        L=Potencia (base, math.floor(exponente/2))
        R=Potencia (base, exponente-math.floor (exponente/2))
        return L * R
