# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:59:05 2020

@author: SELICLO1
"""

#DEBUG = False
DEBUG = True
LOG = True
#LOG = False
if DEBUG: test = open("tests\\01", "r")

class Node:
    """ Class Node to represent a vertex in the de bruijn graph """
    def __init__(self, lab):
        self.label = lab
        self.indegree = 0
        self.outdegree = 0

class Edge:
    def __init__(self, lab):
        self.label = lab

def read_reads():
    if DEBUG:
        reads = [str(line).strip() for line in test.readlines()]
    else:
        reads = input().readlines()
   
    return reads

def construct_graph(reads, k):
    """ Construct de bruijn graph from sets of short reads with k length word"""
    edges = dict()
    vertices = dict()

    for read in reads:
        i = 0
        print(i, "read", read)
        while i+k < len(read):
            v1 = read[i:i+k]
            v2 = read[i+1:i+k+1]
            print("v1", v1, "v2", v2)
            if v1 in edges.keys():
                vertices[v1].outdegree += 1
                edges[v1] += [Edge(v2)]
            else:
                vertices[v1] = Node(v1)
                vertices[v1].outdegree += 1
                edges[v1] = [Edge(v2)]
            if v2 in edges.keys():
                vertices[v2].indegree += 1
            else:
                vertices[v2] = Node(v2)
                vertices[v2].indegree += 1
                edges[v2] = []
            i += 1

    return (vertices, edges)

def output_contigs(g):
    """ Perform searching for Eulerian path in the graph to output genome assembly"""
    V = g[0]
    E = g[1]
    # Pick starting node (the vertex with zero in degree)
    print(V.keys())
    start = V.keys()[0]
    for k in V.keys():
        if V[k].indegree < V[start].indegree:
            start = k

    contig = start
    current = start
    while len(E[current]) > 0:
        # Pick the next node to be traversed (for now, at random)
        next = E[current][0]
        del E[current][0]
        contig += next.label[-1]
        current = next.label

    return contig

def print_graph(g):
    """ Print the information in the graph to be (somewhat) presentable """
    V = g[0]
    E = g[1]
    for k in V.keys():
        print("name: ", V[k].label, ". indegree: ", V[k].indegree, ". outdegree: ", V[k].outdegree)
        print("Edges: ")
        for e in E[k]:
            print(e.label)
        print
        
    
        
# =============================================================================
# # Main
# =============================================================================
#fname = 'tests\\01'
reads = read_reads()

G = construct_graph(reads, 2)
#print_graph(G)
C = output_contigs(G)

#test = ['bcdefg', 'defghi', 'abcd']
# g = construct_graph(test, 3)
#g = db.construct_graph(reads, 11)
# print_graph(g)
# for k in g.keys():
#   print k, g[k]
# g = construct_graph(reads)
#contig = db.output_contigs(g)
#print contig