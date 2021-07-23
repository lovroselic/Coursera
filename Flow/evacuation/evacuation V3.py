# python3

#DEBUG = False
DEBUG = True
LOG = True
#LOG = False
if DEBUG: test = open("tests\\37", "r")

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0
        #self.free = capacity
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
        #self.edges[id].free = self.edges[id].capacity - self.edges[id].flow
        #self.edges[id ^ 1].free = -float("Inf")
        
    def resetVisit(self):
        for i, e in enumerate(self.edges):
            if (i % 2 == 0):
                e.visited = False
            else:
                e.visited = True
        
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
            if LOG: print(u, "from vertice u ->", u+1)
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
        if LOG: print("vertice s:", s)
        while (s != from_):
            for e in graph.graph[parent[s]]:
                if LOG: print("edge index:", e, "from:", graph.graph[parent[s]], graph.edges[e].visited)

                if graph.edges[e].v == s and graph.edges[e].visited == True:
                    free = graph.edges[e].capacity - graph.edges[e].flow
                    print("free:",free)
                    break

            path_flow = min(path_flow, free)
            s = parent[s]
        #
        #break
        
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
