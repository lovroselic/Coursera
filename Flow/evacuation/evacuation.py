# python3

from collections import defaultdict
#DEBUG = False
DEBUG = True
if DEBUG: test = open("tests\\04", "r")

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0
        self.free = capacity

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id].free = self.edges[id].capacity - self.edges[id].flow
        self.edges[id ^ 1].free = self.edges[id ^ 1].capacity - self.edges[id ^ 1].flow
        
    def BFS(self, s, t, parent):
        if DEBUG:print("BFS............")
        visited = [False] * (self.size())
        visited[s] = True
        Q = []
        Q.append(s)
        
        while Q:
            u = Q.pop(0)
            #if DEBUG: print(u, "vertice u ->", u+1)
            for index, edge_index in enumerate(self.graph[u]):
                v = self.edges[edge_index].v
                free = self.edges[edge_index].free
                if visited[v] == False and free > 0:
                    if DEBUG: print(v, "...to vertice v:", v+1)
                    Q.append(v)
                    visited[v] = True
                    parent[v] = u
                    
        #if DEBUG: print(visited)
        if visited[t] == True:
            return True
        else:
            return False

def read_data():
    if DEBUG:
        vertex_count, edge_count = map(int, test.readline().split())
        graph = FlowGraph(vertex_count)
        for _ in range(edge_count):
            u, v, capacity = map(int, test.readline().split())
            graph.add_edge(u - 1, v - 1, capacity)

    else:
        vertex_count, edge_count = map(int, input().split())
        graph = FlowGraph(vertex_count)
        for _ in range(edge_count):
            u, v, capacity = map(int, input().split())
            graph.add_edge(u - 1, v - 1, capacity)
            
    return graph


def max_flow(graph, from_, to):
    flow = 0
    global parent
    parent = [-1] * graph.size()
    # your code goes here
    while graph.BFS(from_, to, parent):
        path_flow = float("Inf")
        s = to
        #if DEBUG: print("s:", s)
        while (s != from_):
            free = -float("Inf")
            for e in graph.graph[parent[s]]:
                print(e, graph.graph[parent[s]])
                #free = -float("Inf")
                if graph.edges[e].v == s:
                    free = max(graph.edges[e].free, free)
                    print("free:",free)
                    #break
            print("last free", free)
            path_flow = min(path_flow, free)
            s = parent[s]
        #
        
        if DEBUG: print("path_flow", path_flow)
        flow += path_flow
        v = to
        
        while (v != from_):
            u = parent[v]
            for e in graph.graph[u]:
                if (graph.edges[e].v == v):
                    graph.add_flow(e, path_flow)
            v = parent[v]
            
            #
            #break
        #
        #break
    #
    return flow


if __name__ == '__main__':
    global graph
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
