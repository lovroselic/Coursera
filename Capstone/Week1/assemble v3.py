# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:11:54 2020

@author: SELICLO1
"""

# =============================================================================
# 
# Use a hashmap/set data structure to remove duplicate reads before proceeding
# Sorting the reads alphabetically with any NlogN sorting algorithm will comfortably simplify the prefix tree construction process - no need to use a Radix sort as recommended by the authors
# Once you find all the suffix-prefix pair matches between reads, you don't need to use a graph data structure to reconstruct the entire genome - just start at the first read, greedily merge it with the highest-overlapping read in its' list of overlapping pairs (that hasn't already been used), then mark the starting read as visited, and continue
# Once all the reads had been used in the reconstruction, use a simple "longest suffix-prefix of a single string" algorithm to trim the ends off the final sequence - this removes the loop from the final read to the first read in the circular sequence
# 
# =============================================================================
NA = -1
numReads = 1618
GSIZE = 5386


#DEBUG = False
DEBUG = True
LOG = True
#LOG = False
#if DEBUG: test = open("tests\\101", "r")
#if DEBUG: test = open("tests\\01", "r")
if DEBUG: test = open("tests\\103.txt", "r")
result = open("tests\\103a.txt", "r").readline()
#if DEBUG: test = open("alice_reads", "r")


def loadReads():
  reads = []
  for _ in range(numReads):
    reads.append(input())

  return reads


def read_reads():
    if DEBUG:
        reads = [str(line).strip() for line in test.readlines()]
    else:
        reads = loadReads()
   
    reads = set(reads)
    return reads

# =============================================================================
# # Overlap -  naive
# =============================================================================

def GreedyNaiveOverlap(PRE, SUF):
    for i in range(len(PRE), 0, -1):
        if PRE[:i] == SUF[len(SUF)-i:]: return i
    return i-1


# =============================================================================
# # Overlap graph
# =============================================================================
class ReadNode:
    def __init__ (self, read):
        self.read = read
        self.visited = False
        self.suf = []
        self.pre = []
        
    def addOverlap(self, overlap, id):
        pass

class Overlap:
    def __init__(self, size, id):
        self.size = size
        self.id = id
    
def CreateGraph(reads):
    ReadMap = []
    for read in reads:
        if DEBUG: print("\nread", read)
        node = ReadNode(read)
        for i, oldRead in enumerate(ReadMap):
            #check pre, set old -> node
            overlap = GreedyNaiveOverlap(node.read, oldRead.read)
            if DEBUG: print(i, "node", node.read, "old", oldRead.read, "overlap", overlap)
    
        ReadMap.append(node)
    return ReadMap

# =============================================================================
# # Main
# =============================================================================

reads = read_reads()
reads = sorted(reads)
#ReadMap = []
GR = CreateGraph(reads)

