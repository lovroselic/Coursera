# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:03:30 2020

@author: SELICLO1
"""
Nucleotides = ['A', 'C', 'G', 'T']

def HammingDistance(a,b):
    mm = 0
    for i,s in enumerate(a):
        if s != b[i]: mm+= 1
    return mm

def Suffix(Pattern):
    return Pattern[1:]

def FirstSymbol(Pattern):
    return Pattern[0]

def Neighbours(Pattern, d):
    #print("..", Pattern)
    if d == 0: return {Pattern}
    if len(Pattern) == 1: return set({'A', 'C', 'G', 'T'})
    Neighborhood = set()
    SuffixNeighbors = Neighbours(Suffix(Pattern), d)
    #print("SuffixNeighbors", SuffixNeighbors)
    #print("Pattern", Pattern)
    for Text in SuffixNeighbors:
        #print("....", Text, " Suffix(Pattern) ", Suffix(Pattern))
        if HammingDistance(Suffix(Pattern), Text) < d:
            for x in Nucleotides:
                Neighborhood.add(x + Text)
                #print(".....", x + Text)
        else:
            Neighborhood.add(FirstSymbol(Pattern) + Text)
            #print(".....", FirstSymbol(Pattern) + Text)
    return Neighborhood

Pattern = 'ACG'
d = 1
result = Neighbours(Pattern, d)
print(" ".join(result))