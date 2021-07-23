#python3


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
        self.in_ = [0] * n
        self.out_ = [0] * n
        self.lower = 0
        self.reads = []
        self.demands = [0] * n
        self.sumT = 0
        #self.conserve = [[0 for _ in range(n+1)] for _ in range(n+1)] 
        

    def add_edge(self, from_, to, capacity, lower):
        forward_edge = Edge(from_, to, capacity-lower)
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
    else:
        vertex_count, edge_count = map(int, input().split())
        
    graph = FlowGraph(vertex_count)
    
    for _ in range(edge_count):
        if DEBUG:
            u, v, lower, capacity = map(int, test.readline().split())
        else:
            u, v, lower, capacity = map(int, input().split())
            
        graph.add_edge(u - 1, v - 1, capacity, lower)
        graph.reads.append((u -1,v -1, lower))
        graph.demands[u-1] += lower
        graph.demands[v-1] -= lower
        #out[from] and in[to].
        graph.out_[u-1] += lower
        #graph.in_[v-1] += lower
        graph.in_[v-1] -= lower
        ##
        graph.lower += lower

            
    return graph
        
# =============================================================================
# def addST(GR):
#     GR.graph.append([])
#     GR.graph.append([])
#     source = len(GR.graph)-2
#     sink = len(GR.graph)-1
#     for i in range(source):
#         demand = GR.demands[i]
#         #print(i, GR.demands[i])
#         if demand < 0: 
#             #add source
#             GR.add_edge(source, i, abs(demand), 0)
#             #print("to source", source, i, abs(demand), 0)
#             GR.sumT += abs(demand)
#             
#         elif demand > 0:
#             #add sink
#             GR.add_edge(i, sink, abs(demand), 0)
#             #print("to sink", i, sink, abs(demand), 0)
# =============================================================================

def addST(GR):
    GR.graph.append([])
    GR.graph.append([])
    source = len(GR.graph)-2
    sink = len(GR.graph)-1
    for i in range(source):
        GR.add_edge(source, i, GR.in_[i], 0)
        print(i, "to source", source, i, -GR.in_[i])
        GR.add_edge(i, sink, GR.out_[i], 0)
        print(i, "to sink", i, sink, GR.out_[i])
        GR.sumT += GR.out_[i]
            

 
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
        
        flow = GR.edges[edgeIndex].flow

        
        print("...ei", edgeIndex, "Flow", GR.edges[edgeIndex].flow, "capacity",GR.edges[edgeIndex].capacity, "lbound",l)
        #print("...Flow", flow, "lbound",l, "conserve", conserve)
        flow = l + flow
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
circulation = result == GR.sumT
if circulation == False:
    print("NO")
    PrintFlow(GR.reads)
else:
    print("YES")
    PrintFlow(GR.reads)
            