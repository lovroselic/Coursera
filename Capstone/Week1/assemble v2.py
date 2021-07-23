# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:11:54 2020

@author: SELICLO1
"""
NA = -1
numReads = 1618
GSIZE = 5386

# =============================================================================
# EulerianCycle(Graph)
# form a cycle Cycle by randomly walking in Graph (don’t visit the same edge twice!)
# while there are unexplored edges in Graph
    # select a vertex newStart in Cycle with still unexplored edges
    # form a cycle Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
    # Cycle ← Cycle’
# return Cycle
# =============================================================================

#DEBUG = False
DEBUG = True
LOG = True
#LOG = False
#if DEBUG: test = open("tests\\101", "r")
if DEBUG: test = open("tests\\01", "r")
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
# # Prefix match - Overlap
# =============================================================================

class Node:
    def __init__ (self):
        self.next = [NA] * 4
        
    def isLeaf(self):
        return self.next[0] == -1 and self.next[1] == -1 and self.next[2] == -1 and self.next[3] == -1
        
def letterToIndex(char):
    if char == "A": return 0
    if char == "C": return 1
    if char == "G": return 2
    if char == "T": return 3
    return None

def build_trie(patterns):
    tree = []
    tree.append(Node())
    for pat in patterns:
        node = 0
        for c in pat:                
            i = letterToIndex(c)
            if tree[node].next[i] != -1:
                node = tree[node].next[i]
            else:
                tree[node].next[i] = len(tree)
                node = len(tree)
                if len(tree) < (node + 1):
                    tree.append(Node())
    return tree


def PrefixMatch(text, trie):
    node = 0
    textIndex = 0
    ci = letterToIndex(text[textIndex])
    while True:  
        if trie[node].isLeaf(): 
            return (True, textIndex)
        elif trie[node].next[ci] != -1:
            node = trie[node].next[ci]
            textIndex += 1
            if textIndex >= len(text):
                return (trie[node].isLeaf(), textIndex)
            ci = letterToIndex(text[textIndex])
        else:
            #return (False, -1)
            return (False, 0)
        
def createPatterns(SUF):
    pat = []
    for p in range(0, len(SUF)):
        pat.append(SUF[p:])
    return pat

# =============================================================================
# def Overlap(PRE, SUF):
#     patterns = createPatterns(SUF)
#     trie = build_trie(patterns)
#     return PrefixMatch(PRE[:len(PRE)-1], trie)
# =============================================================================

def Overlap(PRE, SUF):
    patterns = createPatterns(SUF)
    trie = build_trie(patterns)
    for t in range(len(PRE)-1, -1, -1):
        leaf, overlap = PrefixMatch(PRE[:t+1], trie)
        if overlap > 0: return overlap
    return -1

# =============================================================================
# # Overlap graph
# =============================================================================
class ReadNode:
    def __init__ (self, read):
        self.read = read
        self.visited = False
        self.out = -1
        self.next = None
    
def CreateGraph(reads):
    ReadMap = []
    for read in reads:
        if DEBUG: print("\nread", read)
        node = ReadNode(read)
        #for all
        for i, oldRead in enumerate(ReadMap):
            #check pre, set old -> node
            over = Overlap(node.read, oldRead.read)
            if DEBUG: 
                if over == -1: over = 0
            print(i," .....check old -> node::", "old", oldRead.read, oldRead.out, "new node", node.read, "overlap", over)
                
            if oldRead.out < over:
                oldRead.out = over
                oldRead.next = len(ReadMap)
                print("........updated", oldRead.read, oldRead.out, oldRead.next)
        
            #check suf, node -> old
            over = Overlap(oldRead.read, node.read)
            if DEBUG: 
                if over == -1: over = 0
            print(i, ".....check node -> old::", "new", node.read, node.out, "old", oldRead.read, "overlap", over)
            
                
            if node.out < over:
                node.out = over
                node.next = i
                print("........updated", node.read, node.out, node.next)
                
        ReadMap.append(node)
    return ReadMap

# =============================================================================
# # Main
# =============================================================================

reads = read_reads()
#ReadMap = []
GR = CreateGraph(reads)

