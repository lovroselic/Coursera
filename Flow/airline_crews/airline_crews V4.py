# python3

#DEBUG = False
DEBUG = True
LOG = True
#LOG = False
if DEBUG: test = open("tests\\01x", "r")

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

    def add_edge(self, from_, to, capacity):
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
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        
    def resetVisit(self):
        for e in self.edges: e.visited = False
        
    def BFS(self, s, t, parent):
        if LOG:print("\n")
        if LOG:print("BFS............", s+1, t+1)
        visited = [False] * (self.size())
        visited[s] = True
        self.resetVisit()
        
        Q = []
        Q.append(s)
        
        while Q:
            u = Q.pop(0)
            #if LOG: print(u, "from vertice u ->", u+1)
            for index, edge_index in enumerate(self.graph[u]):
                v = self.edges[edge_index].v
                free = self.edges[edge_index].capacity - self.edges[edge_index].flow
                if LOG: print("  choices:", v+1, "free:", free, "edge index", edge_index)
                if v != u:
                    if (free > 0 and self.edges[edge_index].visited == False and not visited[v]):
                        if LOG: print(v, "...to vertice v:", v+1 , "free:", free)
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

class MaxMatching:
    def read_data(self):
        global adj_matrix
        global graph
        global m
        global n
        
        if DEBUG:
            n, m = map(int, test.readline().split())
            adj_matrix = [list(map(int, test.readline().split())) for i in range(n)]

        else:
            n, m = map(int, input().split())
            adj_matrix = [list(map(int, input().split())) for i in range(n)]
            
        vertex_count = m + n + 2
        graph = FlowGraph(vertex_count)
        #add source
        #n -flights, m - crews
        for i in range(n):
            graph.add_edge(0, i + 1, 1)
        #add flights and crew
        for i in range(n):
            for j in range(m):
                if LOG: print(i, j, ":", adj_matrix[i][j])
                if (adj_matrix[i][j]):
                    u = i + 1;
                    v = j + 1 + n;
                    if LOG: print(u,v)
                    graph.add_edge(u, v, 1)
                    #add sink
                    graph.add_edge(v, m+n+1, 1)  
        
        return graph

    def write_response(self, matching):
        #line = [str(-1 if x == -1 else x + 1) for x in matching]
        line = [str(x) for x in matching]
        print(' '.join(line))

    def solve(self):
        graph = self.read_data()
        flow = max_flow(graph, 0, graph.size() - 1)
        if LOG: print("Flow:", flow)
# =============================================================================
#         if len(matches) < n:
#             for i in range(n - len(matches)):
#                 matches.append(-1)
#                 
#         if len(matches2) < n:
#             for i in range(n - len(matches2)):
#                 matches2.append(-1)
# =============================================================================
                
        #matching = self.find_matching(adj_matrix)
        self.write_response(matches)
        #self.write_response(matches2)

def max_flow(graph, from_, to):
    flow = 0
    global parent
    parent = [-1] * graph.size()
    global matches
    matches = [-1] * n

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
                    #if (s > 0 and s <= n): matches2.append(s)
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
                    if LOG: print("#### adding flow", u, v)
                    #if (u > 0 and u <= n): matches.append(u)
                    #if (u > n): matches2.append(parent[u])
                    if (u > 0 and u <= n): 
                        matches[u-1] = v-n
                        print("............ u  flight", u, " v", v, "crew", v -n)
            v = parent[v]
    return flow


if __name__ == '__main__':
# =============================================================================
#     global matches
#     global matches2
#     matches = []
#     matches2 = []
# =============================================================================
    max_matching = MaxMatching()
    max_matching.solve()
