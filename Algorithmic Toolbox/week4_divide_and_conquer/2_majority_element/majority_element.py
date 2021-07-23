# Uses python3
import sys

# =============================================================================
# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     #write your code here
#     return -1
# =============================================================================

def findMaj(A):
    maj_index = 0
    count = 1
    for i in range(1, len(A)):
        if A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index]
            
def isMajority(A,x):
    count = 0
    for i in range (0, len(A)):
        if A[i] == x:
            count += 1
    if count > len(A) / 2:
        return 1
    else: 
        return -1
    
def get_majority_element(A):
    maj = findMaj(A)
    #print(maj)
    return isMajority(A, maj)
   

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = "5 2 3 9 2 2" 
    #input = "4 1 2 3 1"
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
