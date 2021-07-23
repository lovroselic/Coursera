# python3


#https://www.geeksforgeeks.org/building-heap-from-array/
#https://www.coursera.org/learn/data-structures/lecture/hSzMO/heap-sort

# =============================================================================
#  siftDown(i){
#     let maxIndex = i;
#     let L = this.leftChild(i);
#     if (L <= this.size() - 1 && this.HEAP[L].priority < this.HEAP[maxIndex].priority){
#       maxIndex = L;
#     }
#     let R = this.rightChild(i);
#     if (R <= this.size() - 1 && this.HEAP[R].priority < this.HEAP[maxIndex].priority){
#       maxIndex = R;
#     }
#     if (i !== maxIndex){
#       this.HEAP.swap(i, maxIndex);
#       this.siftDown(maxIndex);
#     }
#   }

# =============================================================================
#  parent(i){
#     return Math.floor((i - 1) / 2);
#   }
#   leftChild(i){
#     return 2 * i + 1;
#   }
#   rightChild(i){
#     return 2 * i + 2;
#   }
# =============================================================================
# =============================================================================

def siftDown(data, index, swaps):
    maxIndex = index
    L = (2 * index) + 1
    if L <= n-1 and data[L] < data[maxIndex]:
        maxIndex = L
    R = (2 * index) + 2
    if R <= n-1 and data[R] < data[maxIndex]:
        maxIndex = R
    if index != maxIndex:
        swaps.append((index, maxIndex))
        data[index], data[maxIndex] = data[maxIndex], data[index]
        siftDown(data, maxIndex, swaps)

def build_heap(data):
    swaps = []
    n = len(data) - 1
    #index = n // 2 - 1
    index = n // 2
    while index >= 0:
        siftDown(data, index, swaps)
        index -= 1
    return swaps
# =============================================================================
# def build_heap(data):
#     """Build a heap from ``data`` inplace.
# 
#     Returns a sequence of swaps performed by the algorithm.
#     """
#     # The following naive implementation just sorts the given sequence
#     # using selection sort algorithm and saves the resulting sequence
#     # of swaps. This turns the given array into a heap, but in the worst
#     # case gives a quadratic number of swaps.
#     #
#     # TODO: replace by a more efficient implementation
#     swaps = []
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] > data[j]:
#                 swaps.append((i, j))
#                 data[i], data[j] = data[j], data[i]
#     return swaps
# =============================================================================


# =============================================================================
# def main():
#     n = int(input())
#     data = list(map(int, input().split()))
#     assert len(data) == n
# 
#     swaps = build_heap(data)
# 
#     print(len(swaps))
#     for i, j in swaps:
#         print(i, j)
# 
# 
# if __name__ == "__main__":
#     main()
# =============================================================================

n = int(input())
data = list(map(int, input().split()))
#n = 5
#data = "5 4 3 2 1"
#data = "1 2 3 4 5"
#data = list(map(int, data.split()))
assert len(data) == n

swaps = build_heap(data)

print(len(swaps))
for i, j in swaps:
    print(i, j)
