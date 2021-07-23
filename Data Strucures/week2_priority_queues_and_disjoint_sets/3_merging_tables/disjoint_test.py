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

def Find(i):
    while i != parent[i]:
        i = parent[i]
    return i

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

LN = 12
parent = makeList(LN+1, 0)
rank = makeList(LN+1, 0)

for i in range(1, LN + 1):
    MakeSet(i)
    
#############
Union(2, 10)
Union(7, 5)
Union(6, 1)
Union(3, 4)
Union(5, 11)
Union(7, 8)
Union(7, 3)
Union(12, 2)
Union(9, 6)
print(Find(6))
print(Find(3))
print(Find(11))
print(Find(9))