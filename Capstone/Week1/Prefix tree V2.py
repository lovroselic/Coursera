# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:24:02 2020

@author: lovro
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4417569/
"""


class Node:
    def __init__ (self, label, id, low, up, chain_len):
        self.label = label
        self.id = id
        self.Lbound = low
        self.Ubound = up
        self.chain_len = chain_len
        self.branch = dict()
        self.remain = None

def PrefixTree(G):
    root = Node("root",-1, -1, -1, -1)
    
    for S in range(0, len(G)):
        #print("\n", S+1, G[S], "\n")
        currentNode = root
        local_position = 1
        path_len = 0
        charPointer = 0
        c = G[S][charPointer]
        #print("Char:", c)
        
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

#text = open("tests/100orig.txt", "r", encoding="utf8") 
#text = open("tests/102.txt", "r", encoding="utf8")
#text = open("tests/102.txt", "r", encoding="utf8")
text = open("tests/103.txt", "r", encoding="utf8")
#text = open("tests/104.txt", "r", encoding="utf8")
#text = open("tests/105.txt", "r", encoding="utf8")


G = [line.strip() for line in text.readlines()]
G = sorted(G)
#G = G[:3]

PT = PrefixTree(G)
