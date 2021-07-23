# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:27:31 2020

@author: SELICLO1
"""

from collections import defaultdict
    
def KmerDict(text, k):
    D = defaultdict(int)
    for i in range(0, len(text) - k + 1):
        kmer = text[i:i+k]
        D[kmer] += 1
    return D

def checkClump(D, t):
    result = []
    for d in D:
        if D[d] >= t: result.append(d)
    return result

def ClumpFinding(genome, K, L, t):
    result = set()
    #init
    D = KmerDict(genome[:L], K)
    result.update(checkClump(D, t))
    first = genome[:K]
    
    for i in range(1, len(genome) - L +1):
        window = genome[i:i+L]
        last = window[-K:]
        D[first] -= 1
        D[last] += 1
        if D[last] >= t: result.add(last)
        first = window[:K]
    
    #return D
    return result
        
        
test = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
K = 5
L = 50
t = 4

# =============================================================================
# test = 'CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG'
# K = 3
# L = 25
# t = 3
# =============================================================================
solution = ClumpFinding(test, K, L, t)
print(" ".join(solution))
