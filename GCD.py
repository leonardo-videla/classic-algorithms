# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:28:07 2021

@author: leona
"""

def GCD (x, y):
    a=x
    b=y
    r=0
    while b != 0:
        q=a//b
        r=a-b*q
        a=b
        b=r
    return a 