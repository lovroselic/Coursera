# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:26:48 2020

@author: lovro
"""

def GreedyNaiveOverlap(PRE, SUF):
    for i in range(len(PRE), 0, -1):
        if PRE[:i] == SUF[len(SUF)-i:]: return i
    return i-1


#print(GreedyNaiveOverlap("CTGAAT", "ACTGAA"))
#print(GreedyNaiveOverlap("CTG", "ATA"))
#print(GreedyNaiveOverlap("TTTCGG", "GGTT"))
print(GreedyNaiveOverlap("GTT", "TCG"))
print(GreedyNaiveOverlap("TCG", "GTT"))
#PRE = "TTTCGG"
#SUF = "GGTT"