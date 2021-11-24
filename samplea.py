# -*- coding: utf-8 -*-
"""
Created on Sun May 23 18:09:12 2021

@author: leona
"""
import numpy as np

def samplea (prob):
    n=len(prob)
    suma=[prob[0]]
    for i in range (1,n):
        suma.append(suma[i-1]+prob[i])
    i=0
    p = np.random.rand()
    while p> suma[i]:
        i=i+1
    return i