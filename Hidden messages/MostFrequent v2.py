# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:27:31 2020

@author: SELICLO1
"""

from collections import defaultdict

def MaxValueDict(D):
    return max(D.values())

def ListOfMax(D, m):
    pats = []
    for d in D:
        if D[d] == m:
            pats.append(d)
    return pats
    
def FrequentWords(text, k):
    D = defaultdict(int)
    for i in range(0, len(text) - k + 1):
        kmer = text[i:i+k]
        D[kmer] += 1
        
    m = MaxValueDict(D)
    pats = ListOfMax(D, m)
    return " ".join(pats)
        
        
test = 'CCAGCGGGGGTTGATGCTCTGGGGGTCACAAGATTGCATTTTTATGGGGTTGCAAAAATGTTTTTTACGGCAGATTCATTTAAAATGCCCACTGGCTGGAGACATAGCCCGGATGCGCGTCTTTTACAACGTATTGCGGGGTAAAATCGTAGATGTTTTAAAATAGGCGTAAC'
K = 5
solution = FrequentWords(test, K)
print(solution)
