# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:53:41 2020

@author: SELICLO1
"""

from collections import defaultdict

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


def MaxValueDict(D):
    return max(D.values())

def ListOfMax(D, m):
    pats = []
    for d in D:
        if D[d] == m:
            pats.append(d)
    return pats
    
def FrequentWordsMismatched(text, k, d):
    D = defaultdict(int)
    for i in range(0, len(text) - k + 1):
        kmer = text[i:i+k]
        NB = Neighbours(kmer, d)
        for nb in NB:
            D[nb] += 1
        
    m = MaxValueDict(D)
    pats = ListOfMax(D, m)
    return pats

def FrequentWordsWithMismatches(Text, k, d):
    pats = FrequentWordsMismatched(Text, k, d)
    print(" ".join(pats))

Text = 'CGACCAGGGTCGTCTAACGTCTAACCGACCGACCGACGCATAACCGACCGACGTCGCAGTCCGACTAACGCACGACGTCTAACTAACGTCCGACGCAGCACAGGCAGGTAACGCATAACTAACGCAGCAGTCGCACGACGCACAGGCGACCGACCGACGTCGTCGCAGCAGTCTAACGCACGACGTCGTCTAACGCAGCATAACCGACGCATAACGTCCGACCAGGCGACTAACTAACGTCGCACGACCGACTAACTAACGCAGCAGCATAACCGACTAACCGACCAGGTAACGTCTAACCGACCAGGCAGGGCAGCACGACGTCGCACAGGTAACCGACTAACCAGGGTCGTCCAGG'
k = 7
d = 2

sol = FrequentWordsWithMismatches(Text, k, d)