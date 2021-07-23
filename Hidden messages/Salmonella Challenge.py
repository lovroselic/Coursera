# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:46:42 2020

@author: SELICLO1
"""
from collections import defaultdict

def RC_char(c):
    if c == 'A': return 'T'
    if c == 'C': return 'G'
    if c == 'G': return 'C'
    if c == 'T': return 'A'
    
def ReverseComplement(string):
    rc = ""
    for c in reversed(string):
        rc += RC_char(c)
    return rc

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
    global D
    D = defaultdict(int)
    for i in range(0, len(text) - k + 1):
        kmer = text[i:i+k]
        NB = Neighbours(kmer, d)
        for nb in NB:
            D[nb] += 1
        RC = Neighbours(ReverseComplement(kmer), d)
        for rc in RC:
            D[rc] += 1
        
    m = MaxValueDict(D)
    pats = ListOfMax(D, m)
    return pats

def FrequentWordsWithMismatchesAndReverseComplements(Text, k, d):
    return FrequentWordsMismatched(Text, k, d)

def readTextFroFile(name, dropHeader = True, join = True):
    lines = []
    with open(name) as file:
        for line in file:
            lines.append(line)
    if dropHeader:
        del(lines[0])
    if join:
        lines = "".join(map(lambda x: x.rstrip("\r\n"), lines))
    return lines
    
def Skew(genome):
    skew = [0]
    for g in genome:
        last = skew[-1]
        if g == 'G': 
            last +=1
        elif g == 'C':
            last -= 1
        skew.append(last)
        
    return skew

def findMin(skew):
    m = min(skew)
    mins = []
    for i,v in enumerate(skew):
        if v == m:
            mins.append(i)
    return mins

def FindMinSkewIndex(genome):
    return findMin(Skew(genome))
    #return " ".join(map(str, indices))
    
fileName = "Salmonella_enterica.txt"
genome = readTextFroFile(fileName)

#genome = 'GATACACTTCCCGAGTAGGTACTG'
minSkew = FindMinSkewIndex(genome)[0]
#print(minSkew)
window = genome[minSkew - 500: minSkew + 500]

sol = FrequentWordsWithMismatchesAndReverseComplements(window, 9, 1)
print(" ".join(sol))