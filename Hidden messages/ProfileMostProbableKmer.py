# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:02:03 2020

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

def readTextFromFile(name):
    with open(name) as file:
        lines = [line for line in file]

    text = lines[0].strip()
    k = int(lines[1])
    profile = {}
    profile['A'] = [float(x) for x in lines[2].split()]
    profile['C'] = [float(x) for x in lines[3].split()]
    profile['G'] = [float(x) for x in lines[4].split()]
    profile['T'] = [float(x) for x in lines[5].split()]
    
    return text, k, profile

# =============================================================================
# profile = {
#     'A': [0.2, 0.2, 0.3, 0.2, 0.3],
#     'C': [0.4, 0.3, 0.1, 0.5, 0.1],
#     'G': [0.3, 0.3, 0.5, 0.2, 0.4],
#     'T': [0.1, 0.2, 0.1, 0.1, 0.2]
# }
# 
# text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
# k = 5
# =============================================================================

# =============================================================================
# profile = {
#     'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
#     'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
#     'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
#     'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
# }
# text = 'AAGTTC'
# pr = ProbabilityKmer(text, profile)
# print(pr)
# =============================================================================


text, k, profile = readTextFromFile('dataset_159_3.txt')
#text, k, profile = readTextFromFile('data2.txt')

s = ProfileMostProbableKmer(text, k, profile)
print(s)
