# Uses python3
import sys
import random

def partition3(a, L, R):
    #write your code here
    x = a[L]
    end = L
    begin = L + 1
    for i in range(L + 1, R + 1):
        if a[i] <= x:
            end += 1
            a[i], a[end] = a[end], a[i]
            if a[end] < x:
                a[begin], a[end] = a[end], a[begin]
                begin += 1
    a[L], a[begin-1] = a[begin - 1], a[L]
    return [begin, end]

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    #m = partition2(a, l, r)
    [m1, m2] = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    #input = "5 2 3 9 2 2"
    #input = "10 2 3 9 2 2 3 4 2 1 2"
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
