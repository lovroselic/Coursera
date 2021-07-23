# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:46:41 2020

@author: SELICLO1
"""

def de_bruijn_ize(st, k):
    edges = []
    nodes = set()
    for i in range(len(st) - k + 1):
        edges.append((st[i:+k-1], st[i+1:i+k]))
        nodes.add(st[i:i+k-1])
        nodes.add(st[i+1:i+k])
    return nodes, edges

nodes, edges = de_bruijn_ize('CCGGTTAAACGTC', 3)
print(nodes)
print(edges)