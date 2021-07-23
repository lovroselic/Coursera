# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:33:09 2020

@author: SELICLO1
"""

from collections import defaultdict

def MaxValueDict(D):
    return max(D.values())

def FirstOfMax(D, m):
    for d in D:
        if D[d] == m:
            return d
    return None

def ListOfMax(D, m):
    pats = []
    for d in D:
        if D[d] == m:
            pats.append(d)
    return pats

def Kmerize(text, k):
    return [text[i:i+k] for i in range(0, len(text) - k + 1)]

def ProbabilityKmer(kmer, profile):
    probability = 1
    for i, k in enumerate(kmer):
        probability *= profile[k][i]
    return probability

def ProfileMostProbableKmer(text, k, profile):
    D = defaultdict(float)
    for kmer in Kmerize(text, k):
        D[kmer] = ProbabilityKmer(kmer, profile)
    
    m = MaxValueDict(D)
    most = FirstOfMax(D, m)
    
    return most

def GreedyMotifSearch(Dna, k, t):
    bestMotifs = list()
    for kmer in Kmerize(Dna[0], k):
        print(kmer)
        
Dna = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
k = 3
t = 5

sol = GreedyMotifSearch(Dna, k, t)