#python3

"""
Created on Fri Jul  3 15:24:02 2020

@author: lovro
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4417569/
"""

DEBUG = True
LOG = False

import itertools
from collections import OrderedDict
numReads = 1618

def loadReads():
  reads = []
  for _ in range(numReads):
    reads.append(input())

  return reads

class Node:
    def __init__ (self, label, id, low, up, chain_len):
        self.label = label
        self.id = id
        self.Lbound = low
        self.Ubound = up
        self.chain_len = chain_len
        self.branch = dict()
        self.remain = None
        
class ReadNode:
    def __init__ (self, id, read):
        self.id = id
        self.read = read
        self.visited = False
        self.overlaps = []
        
    def addOverlap(self, size, id):
        overlap = Overlap(size, id)
        if len(self.overlaps) == 0:
            self.overlaps.append(overlap)
        else:
            for i, over in enumerate(self.overlaps):
                if overlap.size > over.size:
                    self.overlaps.insert(i, overlap)
                    break
            self.overlaps.append(overlap)
            
    def findOverlap(self, id):
        for over in self.overlaps:
            if over.id == id: return over.size
        return None
            
class Overlap:
    def __init__(self, size, id):
        self.size = size
        self.id = id

def FindPSPairs(G, PT):
    for S in range(0, len(G)):
        charPointer = 1

        while charPointer < len(G[S])-1: 
            v = charPointer
            currentNode = PT
            path_len = 0
            local_position = 1
            
            while True:                       
                
                if v == len(G[S])-1:
                    for i in range(currentNode.Lbound, currentNode.Ubound + 1):
                        
                        if GR[i-1][:path_len+1] == G[S][charPointer:]:
                            ReadMap[S].addOverlap(len(G[S]) - charPointer, i-1)
                    break
                
                if currentNode.chain_len >= local_position:
                    g1 = G[S][v]
                    g2 = G[currentNode.Lbound-1][local_position-1]
                    
                    if g1 == g2:
                        local_position +=1
                        path_len +=1
                        v += 1
                    else:
                        break
                else:
                     g1 = G[S][v]

                     if g1 in currentNode.branch.keys(): 
                         currentNode = currentNode.branch[g1]
                         local_position +=1
                         path_len +=1
                         v += 1
                     else:
                         break
            charPointer += 1               

def PrefixTree(G):
    root = Node("root",-1, 1, len(G), 0)
    
    for S in range(0, len(G)):
        currentNode = root
        local_position = 1
        path_len = 0
        charPointer = 0
        c = G[S][charPointer]
        
        while charPointer < len(G[S])-1: 
        
            if currentNode.chain_len >= local_position:
                  
                if c == currentNode.remain[local_position-1]:
                    local_position += 1
                    path_len += 1
                    charPointer += 1
                    c = G[S][charPointer]
                    
                else:
                    v2 =Node(currentNode.remain[local_position-1], currentNode.id, currentNode.Lbound, currentNode.Ubound - 1, currentNode.chain_len - local_position)
                    
                    if v2.chain_len == 0:
                        v2.remain = None
                    else:
                        v2.remain = currentNode.remain[local_position:local_position + v2.chain_len]
                    
                    v2.branch = currentNode.branch.copy()
                    currentNode.branch[v2.label] = v2
                    path_len +=1
                    
                    v3 = Node(c,S, S+1, S+1, len(G[S]) - path_len)
                    
                    if path_len >= len(G[S]):
                        v3.remain = None
                    else:
                        v3.remain = G[S][path_len:]
                        
                    currentNode.branch[v3.label] = v3
                    currentNode.chain_len = local_position - 1
                    
                          
                    if currentNode.chain_len == 0:
                        currentNode.remain = None
                    else:
                        currentNode.remain = currentNode.remain[:currentNode.chain_len]
                        
                    break
            else:
                if c in currentNode.branch.keys():
                    currentNode = currentNode.branch[c]
                    local_position = 1
                    path_len += 1
                    charPointer += 1
                    c = G[S][charPointer]
                    currentNode.Ubound = S + 1
                else:
                    path_len += 1
                    chain_length = len(G[S]) - path_len
                    branch = Node(c, S, S+1, S+1, chain_length)                    
                    currentNode.branch[c] = branch
                    
                    if branch.chain_len == 0:
                        branch.remain = None
                    else:
                        branch.remain = G[S][path_len:]

                    break
    return root

def LSP(S):
    n = len(S)
    lps = [0] * n
    L = 0
    i = 1
    while (i < n):
        if S[i] == S[L]:
            L +=1
            lps[i] = L
            i += 1
        else:
            if L != 0:
                L = lps[L-1]
            else:
                lps[i] = 0
                i += 1
    
    global result
    result = lps[n-1]
    
    if result > n/2:
        return n//2
    else:
        return result
      
def GreedyPath(ReadMap):
    text = ""
    idx = 0
    pre = 0
    while True:
        node = ReadMap[idx]
        if LOG: print(idx, "read", node.read)
        overlap = node.overlaps[0]
        if LOG: print("..overlap to", overlap.id, "weight", overlap.size)
        text += node.read[pre:]
        if LOG: print("text so far", text)
        
        pre = overlap.size
        idx = overlap.id
        if idx == 0: break
    
    lsp_size = LSP(text)
    return text[lsp_size:]

if DEBUG: text = open("tests/110", "r", encoding="utf8")


if DEBUG:
    GR = [line.strip() for line in text.readlines()]
    GR = sorted(GR)
else:
    GR = loadReads()

GR = list(OrderedDict.fromkeys(GR))

ReadMap = [ReadNode(i, read) for i, read in enumerate(GR)]
PT = PrefixTree(GR)
FindPSPairs(GR, PT)
solution = GreedyPath(ReadMap)
print(solution)

