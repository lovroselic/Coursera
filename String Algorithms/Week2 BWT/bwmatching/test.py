# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:49:47 2020

@author: SELICLO1
"""
import itertools


def calcEQ(e, sol):
    sum = 0;
    for i in range (len(e)):
        sum += e[i]*sol[i]
    return sum

e = [-1, -1]
sol = [0, 2]
print(calcEQ(e, sol))