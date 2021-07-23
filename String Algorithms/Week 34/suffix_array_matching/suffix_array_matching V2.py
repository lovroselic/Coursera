# python3
import sys
DEBUG = False
#DEBUG = True
if DEBUG: test = open("sample_tests\\sample2", "r")

def charToIndex(c):
    if c == "A": return 1
    if c == "C": return 2
    if c == "G": return 3
    if c == "T": return 4
    if c == "$": return 0
    return -1

def SortCharacters(S):
    LN = len(S)
    order = [None] * LN
    count = [0] * 5
    for i in range(0, LN):
        count[charToIndex(S[i])] += 1
    for j in range(1,5):
        count[j] = count[j] + count[j-1]
    for i in range(LN - 1, -1, -1):
        c = charToIndex(S[i])
        count[c] -= 1
        order[count[c]] = i
    return order

def ComputeCharClasses(S, order):
    LN = len(S)
    charClass = [None] * LN
    charClass[order[0]] = 0
    for i in range(1, LN):
        if S[order[i]] != S[order[i - 1]]:
            charClass[order[i]] = charClass[order[i - 1]] + 1
        else:
            charClass[order[i]] = charClass[order[i - 1]]
    return charClass

def SortDoubled(S, L, order, charClass):
    LN = len(S)
    newCount = [0] * LN
    newOrder = [None] * LN
    for i in range(0, LN):
        newCount[charClass[i]] += 1
    for j in range (1, LN):
        newCount[j] = newCount[j] + newCount[j-1]   
    for i in range(LN - 1, -1, -1):
        start = (order[i] - L + LN) % LN
        cl = charClass[start]
        newCount[cl] -= 1
        newOrder[newCount[cl]] = start    
    return newOrder

def UpdateClasses(order, charClass, L):
    N = len(order)
    newClass = [None] * N
    newClass[order[0]] = 0
    for i in range(1, N):
        cur = order[i]
        prev = order[i-1]
        mid = (cur + L) % N
        midPrev = (prev + L) % N
        if charClass[cur] != charClass[prev] or charClass[mid] != charClass[midPrev]:
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]
    
    return newClass

def build_suffix_array(text):
    global order
    order = SortCharacters(text)
    charClass = ComputeCharClasses(text, order)
    LN = len(text)
    L = 1
    while L < LN:
        order = SortDoubled(text, L, order, charClass)
        charClass = UpdateClasses(order, charClass, L)
        L *= 2
    return order

def PatternMatching(text, pattern):
    #print("match", pattern, " in ", text)
    PL = len(pattern)
    minIndex = 0
    maxIndex = len(text)
    
    while minIndex < maxIndex:
        midIndex = (minIndex + maxIndex) // 2
        #print(minIndex, maxIndex, midIndex)
        #print(pattern, text[SA[midIndex]:][:PL], pattern > text[SA[midIndex]:][:PL])
        if pattern > text[SA[midIndex]:][:PL]:
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex
            
    start = minIndex
    maxIndex = len(text)
    while minIndex < maxIndex:
        midIndex = (minIndex + maxIndex) // 2
        #print(minIndex, maxIndex, midIndex)
        #print(pattern, text[SA[midIndex]:][:PL], pattern < text[SA[midIndex]:][:PL])
        if pattern < text[SA[midIndex]:][:PL]:
            maxIndex = midIndex
        else:
            minIndex = midIndex + 1
            
    end = maxIndex
    if start >= end:
        return
    else:
        return (start, end)
        
def testSA(text):
    test = []
    for i in SA:
        test.append(text[i:])
    return test

def find_occurrences(text, patterns):
    occs = set()
    for pat in patterns:
        #print(pat)
        #print("==========")
        add = PatternMatching(text, pat)
        #print("add", add)
        if add is not None:
            do = add[0]
            while do < add[1]:
                occs.add(SA[do])
                do +=1
    
    return occs


if __name__ == '__main__':
    if DEBUG:
        text = test.readline().strip()
        pattern_count = int(test.readline().strip())
        patterns = test.readline().strip().split()
        print(text, pattern_count, patterns)
        print("===============")
    else:
        text = sys.stdin.readline().strip()
        pattern_count = int(sys.stdin.readline().strip())
        patterns = sys.stdin.readline().strip().split()
        
    #print(" ".join(map(str, build_suffix_array(text))))
    text = text + "$"
    global SA
    SA = build_suffix_array(text)
    #print(testSA(text))
    
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))
