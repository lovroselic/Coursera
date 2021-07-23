# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 07:28:08 2020

@author: SELICLO1
"""

import math

def SymbolToNumber(c):
    if c == 'A': return 0
    if c == 'C': return 1
    if c == 'G': return 2
    if c == 'T': return 3

def Profile(motifs):
    LN = len(motifs[0])
    count = [[0 for w in range(4)] for q in range(LN)]
    profileMatrix = [[0 for w in range(4)] for q in range(LN)]
    for i in range(LN):
        for m in motifs:
            idx = SymbolToNumber(m[i])
            count[i][idx] += 1
            
    ML = len(motifs)
    for i in range(LN):
        for m in range(4):
            profileMatrix[i][m] = count[i][m] / ML
            
    return profileMatrix

def Consensus(motifs):
    string = ''
    MAP = ['A', 'C', 'G', 'T']
    profileMatrix = Profile(motifs)
    for col in profileMatrix:
        max_val = max(col)
        idx = col.index(max_val)
        string += MAP[idx]
    return string

def Entropy(motifs):
    profileMatrix = Profile(motifs)
    LN = len(motifs[0])
    entropyArray = [None for i in range(LN)]
    for i, col in enumerate(profileMatrix):
        entropy = 0
        for v in col:
            if v < 0.0001: continue
            entropy += v * math.log(v, 2)
        
        entropyArray[i] = -entropy    
    return entropyArray
        


Motifs = ['TCGGGGGTTTTT', 'CCGGTGACTTAC', 'ACGGGGATTTTC', 'TTGGGGACTTTT', 'ATGGGGACTTCC', 'TCGGGGACTTCC', 'TCGGGGATTCAT', 'TAGGGGATTCCT', 'TAGGGGAACTAC', 'TCGGGTATAACC']
mat = Profile(Motifs)
s = Consensus(Motifs)
#print(s)
e = Entropy(Motifs)
print(sum(e))
    
    