# python3
import sys


def compute_min_refills(distance, L, X):
    # write your code here
    numRefills = 0
    currentRefill = 0
    X.append(distance)
    X.insert(0, 0)
    #print(X)
    n = len(X) - 1
    #print("n", n)
    while currentRefill < n:
        lastRefill = currentRefill
        while currentRefill < n and (X[currentRefill+1] - X[lastRefill]) <= L:
            currentRefill += 1
        if currentRefill == lastRefill: return -1
        if currentRefill < n:
            numRefills += 1
    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    #input = "950 400 4 200 375 550 750"
    #input = "10 3 4 1 2 5 9"
    #input = "200 250 2 100 150"
    #d, m, _, *stops = map(int, input.split()) #DEBUG
    #print(d, m, _, stops) #DEBUG
    print(compute_min_refills(d, m, stops))
