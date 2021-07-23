# python3
import collections

def max_sliding_window(sequence, m):
    #if len(sequence) == 1: return  [max(sequence)]
    DQ = collections.deque(range(m))
    maximums = []
    for i in range(m):
        while len(DQ) > 0 and sequence[i] >= sequence[DQ[-1]]:
            DQ.pop()
        DQ.append(i)
    #maximums.append(sequence[DQ[0]])
    for i in range(m, len(sequence)):
        maximums.append(sequence[DQ[0]])
        #remove elements out of window
        while len(DQ) > 0 and DQ[0] <= (i - m): 
            DQ.popleft()
        #remove smaller than currently added
        while len(DQ) > 0 and sequence[i] >= sequence[DQ[-1]]: 
            DQ.pop()
        DQ.append(i)
    maximums.append(sequence[DQ[0]])
    return maximums

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        #print(i)
        maximums.append(max(sequence[i:i + m]))

    return maximums

n = int(input())
input_sequence = [int(i) for i in input().split()]
assert len(input_sequence) == n
window_size = int(input())
    
# =============================================================================
# #n = 6
# n = 1
# #n = 8 
# #input_sequence = "0 1 2 3 4 5".split()
# input_sequence = "1".split()
# #input_sequence = "2 7 3 1 5 2 6 2".split()
# assert len(input_sequence) == n
# #window_size = 2
# #window_size = 4
# window_size = 1
# =============================================================================

#print("naive", *max_sliding_window_naive(input_sequence, window_size))
print(*max_sliding_window(input_sequence, window_size))