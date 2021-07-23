# Uses python3
import sys
import math

def BinarySearch(A, low, high, key):
    if high < low:
        return -1
    if low > high:
        return -1
    mid = low + math.floor((high - low) / 2)
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return BinarySearch(A, low, mid - 1, key)
    else:
        return BinarySearch(A, mid + 1, high, key)

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    return BinarySearch(a, left, right - 1, x)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = "5 1 5 8 12 13 5 8 1 23 1 11"
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    #for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
