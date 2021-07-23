# Uses python3
import sys
import itertools

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

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
# =============================================================================
#     input = '''
#     11
#     17 59 34 57 17 23 67 1 18 2 59
#     '''
#     input = '''
#     4
#     3 3 3 3
#     '''
# =============================================================================
    n, *A = list(map(int, input.split()))
    print(partition3(A))

