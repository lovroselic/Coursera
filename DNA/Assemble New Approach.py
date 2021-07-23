# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:37:14 2020

@author: SELICLO1
"""

#from itertools import permutations
from collections import defaultdict
filename = "ads1_week4_reads.fq"

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

def overlap(a, b, min_length=3):
    start = 0  
    while True:
        start = a.find(b[:min_length], start)  
        if start == -1: 
            return 0
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1 
        
def createKMerDict(reads, k):
    D = defaultdict(set)
    for r in reads:
        for i in range(0, len(r)-k +1):
            kmer = r[i:i+k]
            D[kmer].add(r)
    return D
    
def Overlap_all_pairs(reads, min_length = 30):
    D = createKMerDict(reads, k)
    overlap_graph = defaultdict(set)
    for read in reads:
        read_suffix = read[-min_length:]
        readSet = D[read_suffix]
        readSet.discard(read)
        for B in readSet:
            olap = overlap(read, B, min_length)
            if olap > 0:
                overlap_graph[(read,B)] = olap
    return overlap_graph
    
def pick_max_overlap_fast(GR):
    if len(GR) == 0: return 0, 0, 0
    max_key = max(GR, key=lambda k: GR[k])
    A = max_key[0]
    B = max_key[1]
    olap = GR[max_key]
    GR.pop(max_key)
    return A, B, olap

def greedy_scs(reads,k):
    GR = Overlap_all_pairs(reads, k)
    readA, readB, olen = pick_max_overlap_fast(GR)
    while olen > 0:
        reads.remove(readA)
        reads.remove(readB)
        reads.append(readA + readB[olen:])
        GR = Overlap_all_pairs(reads, k)
        readA, readB, olen = pick_max_overlap_fast(GR)
    return ''.join(reads)



# =============================================================================
# # Main
# =============================================================================
reads,_ = readFastq(filename)
#reads = ["ABC", "BCD", "CDE", "DEFG", "FGH"]
k = 30
genome = greedy_scs(reads,k)
GL = len(genome)
print(GL)
counts = defaultdict(int)
for L in genome:
    counts[L] +=1
    
print(counts)