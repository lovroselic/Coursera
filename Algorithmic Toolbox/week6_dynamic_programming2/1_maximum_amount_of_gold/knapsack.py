# Uses python3
import sys

# =============================================================================
# def optimal_weight(W, w):
#     # write your code here
#     result = 0
#     for x in w:
#         if result + x <= W:
#             result = result + x
#     return result
# =============================================================================

# =============================================================================
# def optimal_weight(W, w):
#     # with repetitions
#     print(w, W)
#     global value
#     value = [0 for w in range(W+1)]
#     result = 0
#     for weight in range(1,W+1):
#         print("weight", weight)
#         value[weight] = 0
#         for i in range(len(w)):
#             print("...", w[i], weight, "val[w]", value[weight])
#             if (w[i] <= weight):
#                 val = value[weight - w[i]] + w[i]
#                 print("val", val, value[weight])
#                 if val > value[weight]:
#                     value[weight] = val
#     return value
# =============================================================================

def optimal_weight(W, w):
    #global Matrix
    Matrix = [[0 for i in range(len(w)+1)] for j in range(W+1)]
    for bar in range(1, len(w)+1):
        for weight in range(1, W+1):
            Matrix[weight][bar] = Matrix[weight][bar -1]
            if w[bar-1] <= weight:
                val = Matrix[weight - w[bar-1]][bar -1] + w[bar-1]
                if val > Matrix[weight][bar]:
                    Matrix[weight][bar] = val
    return Matrix[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
# =============================================================================
#     input = '''
#     10 3
#     1 4 8
#     '''
# =============================================================================
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
