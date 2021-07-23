# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:35:07 2020

@author: SELICLO1
"""
from itertools import permutations
from collections import defaultdict

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
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match
        
def naive_overlap_map(reads,k):
    olaps = {}
    for a,b in permutations(reads,2):
        olen = overlap(a,b, min_length = k)
        if olen > 0:
            olaps[(a,b)] = olen
    return olaps

def createKMerDict(reads, k):
    D = defaultdict(set)
    for r in reads:
        for i in range(0, len(r)-k +1):
            kmer = r[i:i+k]
            D[kmer].add(r)
    return D
    
def Overlap_all_pairs(reads, D, min_length = 30):
    overlap_graph = defaultdict(set)
    for read in reads:
        read_suffix = read[-min_length:]
        #print(read, read_suffix)
        readSet = D[read_suffix]
        readSet.remove(read)
        #print("..", readSet)
        for B in readSet:
            #print("....compar to", B)
            olap = overlap(read, B, min_length)
            #print(".....olap", olap)
            if olap > 0:
                overlap_graph[(read,B)] = olap
    return overlap_graph


def countActiveNodes(GR):
    nodes = defaultdict(int)
    for edge in GR:
        node = edge[0]
        nodes[node] += 1
    return nodes
# =============================================================================
# # MAin
# =============================================================================

#reads = ['CGTACG', 'TACGTA', 'GTACGT', 'ACGTAC', 'GTACGA', 'TACGAT']
filename = "ERR266411_1.for_asm.fastq"
reads,_ = readFastq(filename)
#text = open(filename, "r", encoding="utf8")
#reads = [line.strip() for line in text.readlines()]

K = 30
D = createKMerDict(reads, K)
GR = Overlap_all_pairs(reads, D, K)
print("q3", len(GR))
ND = countActiveNodes(GR)
print("q4", len(ND))

