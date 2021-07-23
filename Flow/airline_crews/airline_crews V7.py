# python3

DEBUG = False
#DEBUG = True
#LOG = True
LOG = False
if DEBUG: test = open("tests\\02", "r")

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
        visited = [False] * (self.size())
        visited[s] = True
        self.resetVisit()
        
        Q = []
        Q.append(s)
        
        while Q:
            u = Q.pop(0)
            for index, edge_index in enumerate(self.graph[u]):
                v = self.edges[edge_index].v
                free = self.edges[edge_index].capacity - self.edges[edge_index].flow
                if v != u:
                    if (free > 0 and self.edges[edge_index].visited == False and not visited[v]):
                        Q.append(v)
                        visited[v] = True
                        self.edges[edge_index].visited = True
                        parent[v] = u
            if visited[t] == True: break
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

        for i in range(n):
            graph.add_edge(0, i + 1, 1)
            if LOG: print(0, i + 1)

        for i in range(n):
            for j in range(m):
                if (adj_matrix[i][j]):
                    u = i + 1;
                    v = j + 1 + n;
                    if LOG: print(u,v)
                    graph.add_edge(u, v, 1)
        #add sink
        for c in range(n + 1, n + m + 1):
            graph.add_edge(c, m + n + 1, 1) 
            if LOG: print(c, m + n + 1)
        return graph

    def write_response(self, matching):
        line = [str(x) for x in matching]
        print(' '.join(line))
        
    def find_matching(self, graph):
        matching = [-1] * n
        for c in range(1, n+1):
            edges = graph.graph[c]
            for edge in edges:
                if edge % 2 == 0:
                    if graph.edges[edge].flow == 1:
                        matching[c-1] = graph.edges[edge].v - n
                        if LOG: print("edge", graph.edges[edge].u, graph.edges[edge].v, "flow", graph.edges[edge].flow)
        return matching

    def solve(self):
        graph = self.read_data()
        flow = max_flow(graph, 0, graph.size() - 1)
        if LOG: print("Flow:", flow)           
        matching = self.find_matching(graph)
        self.write_response(matching)

def max_flow(graph, from_, to):
    flow = 0
    global parent
    parent = [-1] * graph.size()

    while graph.BFS(from_, to, parent):
        path_flow = float("Inf")
        s = to
        while (s != from_):
            for e in graph.graph[parent[s]]:
                if graph.edges[e].v == s and graph.edges[e].visited == True:
                    free = graph.edges[e].capacity - graph.edges[e].flow
                    break
            path_flow = min(path_flow, free)
            s = parent[s]
        flow += path_flow
        v = to
        
        while (v != from_):
            u = parent[v]
            for e in graph.graph[u]:
                if (graph.edges[e].v == v and graph.edges[e].visited == True):
                    graph.add_flow(e, path_flow)
                    if LOG: print("#### adding flow", u, v)                   
            v = parent[v]
    return flow


if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
