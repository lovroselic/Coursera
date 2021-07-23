#python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:24:02 2020

@author: lovro
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4417569/
"""
import random

def RandomReads(text, K):
    LN = len(text+text)
    K = 4
    readN = int(round(LN/K, 0)) ** 2
    reads = []
    for r in range(readN):
        r = random.randint(0, len(text) - K)
        reads.append(text[r:r+K])
    return reads

result = open("tests\\109a.txt", "r").readline()

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
            #we don't need all overlaps
            self.overlaps.append(overlap)
class Overlap:
    def __init__(self, size, id):
        self.size = size
        self.id = id

def FindPSPairs(G, PT):
    for S in range(0, len(G)):
        #print("\n", S+1, G[S], "\n")
        charPointer = 1

        while charPointer < len(G[S])-1: 
            #print("\n########### charPointer", charPointer, G[S][charPointer], "suffix", G[S][charPointer:])
            v = charPointer
            currentNode = PT
            path_len = 0
            local_position = 1
            
            while True:                       
                #print("\n", G[S][v], v)
                
                if v == len(G[S])-1:
                    #we have a pS match in range
                    #print("checking for a PS match in range:", currentNode.Lbound, currentNode.Ubound, "CL", currentNode.chain_len)
                    for i in range(currentNode.Lbound, currentNode.Ubound + 1):
                        #print("....compare string", GR[i-1], "suffix", GR[i-1][:path_len+1],"to:", G[S][charPointer:])
                        
                        if GR[i-1][:path_len+1] == G[S][charPointer:]:
                            print("!!MATCH!!:", GR[i-1], "has prefix", G[S], "has suffix; length of overlap ", len(G[S]) - charPointer)
                            print("idx", S, "->", i-1)
                            
                            ReadMap[S].addOverlap(len(G[S]) - charPointer, i-1)
                            

                    break
                #endif
                #print("...current node::", currentNode.label, currentNode.Lbound, currentNode.Ubound, currentNode.chain_len)
                #print("local_position", local_position)
                if currentNode.chain_len >= local_position:
                    g1 = G[S][v]
                    g2 = G[currentNode.Lbound-1][local_position-1]
                    #print("G1", g1)
                    #print("G2", g2)
                    #print("currentNode.chain_len >= local_position", currentNode.chain_len , local_position, "g1,g2", g1, g2)
                    if g1 == g2:
                        local_position +=1
                        path_len +=1
                        v += 1
                    else:
                        break
                else:
                     g1 = G[S][v]
                     #print("se<rching for branch", g1, ":", currentNode.branch.keys())
                     if g1 in currentNode.branch.keys(): 
                         currentNode = currentNode.branch[g1]
                        # print("branched to:", currentNode.label, currentNode.Lbound, currentNode.Ubound, currentNode.chain_len)
                         local_position +=1
                         path_len +=1
                         v += 1
                         #print("v increased to", v)
                     else:
                         #print("no branch")
                         break
                #endif
            #end while
            charPointer += 1 
        #end while
    #end for
                


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
                    #print("  EQUAL  ", c, currentNode.remain[local_position-1])
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
                    
                    #print("creating new node v2", v2.label, v2.Lbound, v2.Ubound, "ChainLen:", v2.chain_len, "remain", v2.remain)
                    v2.branch = currentNode.branch.copy()
                    currentNode.branch[v2.label] = v2
                    path_len +=1
                    
                    v3 = Node(c,S, S+1, S+1, len(G[S]) - path_len)
                    
                    if path_len >= len(G[S]):
                        v3.remain = None
                    else:
                        v3.remain = G[S][path_len:]
                        
                    #print("creating new node v3", v3.label, v3.Lbound, v3.Ubound, "ChainLen:", v3.chain_len, "remain", v3.remain)
                    currentNode.branch[v3.label] = v3
                    currentNode.chain_len = local_position - 1
                    
                          
                    if currentNode.chain_len == 0:
                        currentNode.remain = None
                    else:
                        currentNode.remain = currentNode.remain[:currentNode.chain_len]
                        
                    #print("old currentNode", currentNode.label, currentNode.Lbound, currentNode.Ubound, "ChainLen:", currentNode.chain_len, "remain", currentNode.remain)
                    break
            else:
                if c in currentNode.branch.keys():
                    currentNode = currentNode.branch[c]
                    #print("changed to node", currentNode.label,"currentNode.chain_len:", currentNode.chain_len, "\n")
                    local_position = 1
                    path_len += 1
                    charPointer += 1
                    c = G[S][charPointer]
                    currentNode.Ubound = S + 1
                else:
                    #print("NO BRANCH!")
                    path_len += 1
                    chain_length = len(G[S]) - path_len
                    branch = Node(c, S, S+1, S+1, chain_length)                    
                    currentNode.branch[c] = branch
                    
                    if branch.chain_len == 0:
                        branch.remain = None
                    else:
                        branch.remain = G[S][path_len:]

                    #print("creating NEW NODE", branch.label, branch.Lbound, branch.Ubound, "ChainLen:", branch.chain_len, "remain", branch.remain)
                    break
    return root

def FindNextUnvisited():
    for i, v in enumerate(visitMatrix):
        if v : return i
    return False

def NaiveReconstruct(ReadMap):
    print("\nReconstruction .....")
    global visitMatrix
    visitMatrix = [False]* len(ReadMap)
    
    start = random.randint(0, len(ReadMap) - 1)
    #start = 0
    print("starting at", start)
    read = ReadMap[start]
    
    global text
    text = ""
    text = read.read
    count = 0
    while True:
        print("\nread", read.id, read.read)
        print("text so far", text)
        #visitMatrix[read.id] = True
        #get greediest non visited overlap
        while True:
            if len(read.overlaps) == 0: break
            overlap = read.overlaps.pop()
            if visitMatrix[overlap.id] == False:
                print("overlap", overlap.size, overlap.id, "remaining", len(read.overlaps))
                nextRead = ReadMap[overlap.id]
                visitMatrix[overlap.id] = True
                break
        print("nextRead", nextRead.read)
        text += nextRead.read[overlap.size:]
        read = nextRead
        
        count += 1
        if count == len(GR): break
    return text
        

    

#text = open("tests/100orig.txt", "r", encoding="utf8") 
#text = open("tests/102.txt", "r", encoding="utf8")
#text = open("tests/102.txt", "r", encoding="utf8")
text = open("tests/109.txt", "r", encoding="utf8")
#text = open("tests/104.txt", "r", encoding="utf8")
#text = open("tests/105.txt", "r", encoding="utf8")
#text = open("tests/106.txt", "r", encoding="utf8")

#result = "ACGTAGC"
#K = 4
#GR = RandomReads(result, K)
#GR = ['ACGT', 'CGTA', 'GTAG', 'TAGC', 'GCAC']


GR = [line.strip() for line in text.readlines()]
GR = sorted(GR)
GR = sorted(list(set(GR)))

ReadMap = [ReadNode(i, read) for i, read in enumerate(GR)]
PT = PrefixTree(GR)
FindPSPairs(GR, PT)

solution = NaiveReconstruct(ReadMap)
print("solution", solution)

