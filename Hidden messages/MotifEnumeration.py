# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:09:32 2020

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
    if d == 0: return {Pattern}
    if len(Pattern) == 1: return set({'A', 'C', 'G', 'T'})
    Neighborhood = set()
    SuffixNeighbors = Neighbours(Suffix(Pattern), d)
    for Text in SuffixNeighbors:
        if HammingDistance(Suffix(Pattern), Text) < d:
            for x in Nucleotides:
                Neighborhood.add(x + Text)
        else:
            Neighborhood.add(FirstSymbol(Pattern) + Text)
    return Neighborhood

def Kmerize(text, k):
    return [text[i:i+k] for i in range(0, len(text) - k + 1)]
    
def MotifEnumeration(Dna, k, d):
    Patterns = [set() for i in range(len(Dna))]
    for i, text in enumerate(Dna):
        for kmer in Kmerize(text, k):
            for pat in Neighbours(kmer, d):
                Patterns[i].add(pat)

    inter = list(set.intersection(*Patterns))
    return inter
    
Dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
k = 3
d = 1

sol = MotifEnumeration(Dna, k, d)
print(" ".join(sol))