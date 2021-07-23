# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:05:37 2020

@author: lovro
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
nodes = list(nodes)
print(nodes[0])