#python3

'''
Modify edge capacities - decrease by flow lower bound (because we assume in this model that it's already flowing through when we calculate)
Connect target that "sucks away" the flow lower bound from each edge beginning. (As we know these are all directed edges.)
Connect source that "pushes in" the flow lower bound to each edge end.
Solve for max flow
Add flow lower bound to edge capacities (i.e. revert to original value) and flows to get the correct flow value.
If the max flow value equals the sum of flow lower bounds, then the circulation exists.
'''

'''
1. reduce the original problem to circulation with demands but with zero lower bounds problem 
(by changing capacity to capacity - lowerBound, and
 
 adding demand for each vertex).

2. add a source vertex and a sink vertex to further reduce the problem to maxFlow problem.
'''
'''
natalia:
I created a graph for maxFlow as was suggested in Course 5, all edges with even ids were forward edges, edges with odd ids - backward.
When restoring path I calculated reverse edgeId as (edgeId +1) instead of (edgeId ^ 1). If a path has a reverse edge in it (id=3, for example), 
reverse one to it should be 2, not 4.

My data structure for storing the graph is the same as in the starter files for MaxFlow Problem from Course 5: 
    a list with edges, and an array of n lists (n - number of vertices) which store ids of the edges outgoing from i-th node.
    
DONE: I populated the graph with the edges with capacity (c - l), 
??? : and added the lower bound of the edge to two arrays: out[from] and in[to].

After I processed all edges from the input, I added two vertices to the graph - s and t.
 And after that for each vertex I added two edges:

s -> v with capacity in[v]
v-> t with capacity out[v]


After that I ran MaxFlow algorithm and compared the MaxFlow with the sum of lower bounds. If they are equal, that means that we have a solution. 
I output used units of flow (use the edges in the residual network) plus the lower bound of the edge.
'''

# do I need to add flow to s -> u?
# what about backward edge
# https://github.com/SleekPanther/circulation-with-demands-network-flow
# supply and demand vertices!

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0
        self.visited = False

class FlowGraph:

    def __init__(self, n):
        self.edges = []
        self.graph = [[] for _ in range(n)]
# =============================================================================
#         self.in_ = [0] * (n +2)
#         self.out_ = [0] * (n +2)
# =============================================================================
        self.in_ = [0] * n
        self.out_ = [0] * n
        self.lower = 0
        self.reads = []

    def add_edge(self, from_, to, capacity, lower):
        #forward_edge = Edge(from_, to, capacity)
        forward_edge = Edge(from_, to, capacity-lower)
        backward_edge = Edge(to, from_, 0)
        #backward_edge = Edge(to, from_, -lower)
        
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)
        #
        # =============================================================================
        # Connect target that "sucks away" the flow lower bound from each edge beginning
        # Connect source that "pushes in" the flow lower bound to each edge end.
        # =============================================================================
# =============================================================================
#         if lower == 0:return
#         self.in_[to] = lower
#         self.out_[from_] = lower
#         self.lower += lower
# =============================================================================

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        
    def resetVisit(self):
        for e in self.edges: e.visited = False
        
    def BFS(self, s, t, parent):
        if LOG:print("\n")
        if LOG:print("BFS............", s, t)
        visited = [False] * (self.size())
        visited[s] = True
        self.resetVisit()
        
        Q = []
        Q.append(s)
        
        while Q:
            u = Q.pop(0)
            if LOG: print(u, "from vertice u ->", u)
            for index, edge_index in enumerate(self.graph[u]):
                v = self.edges[edge_index].v
                free = self.edges[edge_index].capacity - self.edges[edge_index].flow
                if LOG: print("  choices:", v, "free:", free, "edge index", edge_index)
                if v != u:
                    if (free > 0 and self.edges[edge_index].visited == False and not visited[v]):
                        if LOG: print(v, "...to vertice v:", v , "free:", free)
                        Q.append(v)
                        visited[v] = True
                        self.edges[edge_index].visited = True
                        parent[v] = u
            if visited[t] == True: break

        
        if LOG: print(".................")
        if LOG: print("\n")
        if visited[t] == True:
            return True
        else:
            return False

def read_data():
    if DEBUG:
        vertex_count, edge_count = map(int, test.readline().split())
        graph = FlowGraph(vertex_count)
        for _ in range(edge_count):
            u, v, lower, capacity = map(int, test.readline().split())
            graph.add_edge(u - 1, v - 1, capacity, lower)
            graph.reads.append((u -1,v -1, lower))
            #
            graph.lower += lower
            graph.in_[v-1] += lower
            graph.out_[u-1] += lower
            #graph.out_[u-1] -= lower

    else:
        vertex_count, edge_count = map(int, input().split())
        graph = FlowGraph(vertex_count)
        for _ in range(edge_count):
            u, v, lower, capacity = map(int, input().split())
            graph.add_edge(u - 1, v - 1, capacity, lower)
            graph.reads.append((u -1,v -1, lower))
            
    return graph

def addST(GR):
    #add source S
    GR.graph.append([])
    #add sink T
    GR.graph.append([])
    #s -> v with capacity in[v]
    #v-> t with capacity out[v]
    source = len(GR.graph)-2
    sink = len(GR.graph)-1
    for i in range(len(GR.graph)-2):
        
        GR.add_edge(source, i, GR.in_[i], 0)
        print("to source", source, i, GR.in_[i])
        GR.add_edge(i, sink, GR.out_[i], 0)
        print("to sink", i, sink, GR.out_[i], 0)

 
def max_flow(graph, from_, to):
    flow = 0
    global parent
    parent = [-1] * graph.size()

    while graph.BFS(from_, to, parent):
        path_flow = float("Inf")
        s = to
        if LOG: print("vertice s:", s)
        while (s != from_):
            for e in graph.graph[parent[s]]:
                if LOG: print("edge index:", e, "from:", graph.graph[parent[s]], graph.edges[e].visited)

                if graph.edges[e].v == s and graph.edges[e].visited == True:
                    free = graph.edges[e].capacity - graph.edges[e].flow
                    if LOG: print("free:",free)
                    break

            path_flow = min(path_flow, free)
            s = parent[s]
        
        if LOG: print("path_flow", path_flow)
        if LOG: print("---------------")
        flow += path_flow
        v = to
        
        while (v != from_):
            u = parent[v]
            for e in graph.graph[u]:
                if (graph.edges[e].v == v and graph.edges[e].visited == True):
                    graph.add_flow(e, path_flow)
            v = parent[v]
    return flow

def PrintFlow(reads):
    
    def findindex(edges, u, v):
        for e in edges:
            if e % 2 == 0:
                if GR.edges[e].u == u and GR.edges[e].v == v:
                    return e
        return None
                
    for r in reads:
        u,v,l = map(int, r)
        #print(r, u, v, l)
        edges = GR.graph[u]
        #print("..edges", edges)
        edgeIndex = findindex(edges, u, v)
        #print("...ei", edgeIndex, GR.edges[edgeIndex].flow, l)
        flow = l + GR.edges[edgeIndex].flow
        print(flow)
    
# =============================================================================
# # MAIN
# =============================================================================

DEBUG = True
LOG = False
if DEBUG: test = open("tests\\c02", "r")
GR = read_data()
addST(GR)
result = max_flow(GR, GR.size() - 2, GR.size() - 1)
circulation = result == GR.lower
if circulation == False:
    print("NO")
    PrintFlow(GR.reads)
else:
    print("YES")
    PrintFlow(GR.reads)
            