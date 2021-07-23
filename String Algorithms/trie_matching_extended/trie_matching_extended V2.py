# python3
import sys

#DEBUG = False
DEBUG = True
if DEBUG: test = open("sample_tests\\sample11", "r")
#0 1 2 3 6 7 8 11 12 15
#0 1 2 3 6 7 8 11 12 15
#0 1 2 3 5 6 7 8 10 11 12 14 15

NA = -1

class Node:
    def __init__ (self):
        self.next = [NA] * 4
        self.patternEnd = [False] * 4
        
    def isLeaf(self):
        return self.next[0] == -1 and self.next[1] == -1 and self.next[2] == -1 and self.next[3] == -1
        
def letterToIndex(char):
    if char == "A": return 0
    if char == "C": return 1
    if char == "G": return 2
    if char == "T": return 3
    return None

def build_trie(patterns):
    tree = []
    tree.append(Node())
    for pat in patterns:
        #if DEBUG: print(pat)
        node = 0
        #for c in pat:
        for ci in range(len(pat)):
            c = pat[ci]                
            i = letterToIndex(c)
            if tree[node].next[i] != -1:
                if ci == len(pat) - 1:
                    tree[node].patternEnd[i] = True
                node = tree[node].next[i]
            else:
                tree[node].next[i] = len(tree)
                
                node = len(tree)
                if len(tree) < (node + 1):
                    tree.append(Node())
    return tree


def PrefixMatch(text, trie):
    #if DEBUG: print(text)
    node = 0
    textIndex = 0
    ci = letterToIndex(text[textIndex])
    while True:  
        if trie[node].isLeaf(): 
            #if DEBUG: print("leaf")
            return True
        elif trie[node].next[ci] != -1:
            if (trie[node].patternEnd[ci]):
                #if DEBUG: print("PE", node)
                return True
            node = trie[node].next[ci]
            textIndex += 1
            if textIndex >= len(text):
                return trie[node].isLeaf()
            ci = letterToIndex(text[textIndex])
        else:
            return False
        

def solve (text, n, patterns):
    result = []
    global trie
    trie = build_trie(patterns)
    if DEBUG: print("--------------")
    for t in range(len(text)):
        if PrefixMatch(text[t:], trie): result.append(t)
    return result


if DEBUG: 
    text = test.readline ().strip ()
else:
    text = sys.stdin.readline ().strip ()

if DEBUG:
    n = int (test.readline ().strip ())
else:
    n = int (sys.stdin.readline ().strip ())
if DEBUG: print(text, n)
patterns = []
for i in range (n):
    if DEBUG:
        patterns += [test.readline ().strip ()]
    else:
        patterns += [sys.stdin.readline ().strip ()]
if DEBUG: print(patterns)
ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
