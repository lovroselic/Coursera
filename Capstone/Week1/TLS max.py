# python3
#https://www.youtube.com/watch?v=-JjA4BLQyqE&t=534s


#DEBUG = False
DEBUG = True
LOG = True
#LOG = False
if DEBUG: test = open("tests\\01TLS", "r")

import itertools
INF = 10 ** 9

def read_data():
    if DEBUG:
        n, m = map(int, test.readline().split())
    else:
        n, m = map(int, input().split())
        
    graph = [[-1] * n for _ in range(n)]
    for _ in range(m):
        if DEBUG:
            u, v, weight = map(int, test.readline().split())
        else:
            u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))

def held_karp(graph):
    n = len(graph)
    global C
    C = {}
    
    for k in range(1, n):
        C[(1 << k, k)] = (graph[0][k], 0)
    
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev = bits & ~(1 << k)
                global res
                res = []
                for m in subset:
                    if m == 0 or m == k: continue
                    res.append((C[(prev, m)][0] + graph[m][k], m))
                C[(bits, k)] = max(res)
                
    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + graph[k][0], k))
    opt, parent = max(res)
    if opt <= -1:
        return (-1, [])
    
    global path
    path = []
    for i in range(n - 1):
        path.append(parent+1)
        new_bits = bits & ~(1 << parent)
        temp, parent = C[(bits, parent)]
        bits = new_bits
    path.append(1)
    
    return (opt, list(reversed(path)))


# =============================================================================
# ## main
# =============================================================================

graph = read_data()
path2 = held_karp(graph)
print_answer(*path2)


