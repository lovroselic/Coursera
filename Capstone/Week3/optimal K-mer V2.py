#python3
from collections import OrderedDict


DEBUG = True
LOG = False

def loadReads():
  reads = []
  for _ in range(numReads):
    reads.append(input())

  return reads
# =============================================================================
# 
# =============================================================================

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
        
        while charPointer < len(G[S]): 
        
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

def findK(Readmap):
    minO = 100
    for r in Readmap:
        #print(r.overlaps[0].size)
        minO = min(minO, r.overlaps[0].size)
    
    return minO

# =============================================================================
# # main
# =============================================================================


if DEBUG: test = open("tests/01", "r", encoding="utf8")
numReads = 400

if DEBUG:
    reads = [line.strip() for line in test.readlines()]
else:
    reads = loadReads()
    
K = len(reads[0])

GR = list(OrderedDict.fromkeys(sorted(reads)))
ReadMap = [ReadNode(i, read) for i, read in enumerate(GR)]
PT = PrefixTree(GR)
FindPSPairs(GR, PT)
print(findK(ReadMap)+1)