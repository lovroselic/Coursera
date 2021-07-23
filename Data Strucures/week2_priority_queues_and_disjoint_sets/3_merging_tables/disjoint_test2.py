# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:10:40 2019

@author: SELICLO1
"""

def makeList(ln, iv):
    return [iv for x in range(ln)]

def MakeSet(i):
    parent[i] = i
    rank[i] = 0

# =============================================================================
# def Find(i):
#     while i != parent[i]:
#         i = parent[i]
#     return i
# =============================================================================
    
def Find(i):
    #/w path compression
    if i != parent[i]:
        parent[i] = Find(parent[i])
    return parent[i]

def Union(i, j):
    i_id = Find(i)
    j_id = Find(j)
    if i_id == j_id: return
    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1

LN = 60
parent = makeList(LN+1, 0)
rank = makeList(LN+1, 0)

for i in range(1, LN + 1):
    MakeSet(i)
    
for i in range(1,31):
    Union(i, 2 * i)
    
for i in range(1,21):
    Union(i, 3 * i)
    
for i in range(1,13):
    Union(i, 5 * i)
    
for i in range(1, LN + 1):
    Find(i)
    