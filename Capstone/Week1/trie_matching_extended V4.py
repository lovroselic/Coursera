
NA = -1
DEBUG = True

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
        node = 0
        for ci in range(len(pat)):
            c = pat[ci]                
            i = letterToIndex(c)
            if ci == len(pat) - 1:
                tree[node].patternEnd[i] = True
            if tree[node].next[i] != -1:
                node = tree[node].next[i]
            else:
                tree[node].next[i] = len(tree)
                node = len(tree)
                if len(tree) < (node + 1):
                    tree.append(Node())
    return tree


def PrefixMatch(text, trie):
    #if DEBUG: print("matching", text)
    node = 0
    textIndex = 0
    ci = letterToIndex(text[textIndex])
    while True:  
        if trie[node].isLeaf(): 
            return True
        elif trie[node].next[ci] != -1:
            if (trie[node].patternEnd[ci]):
                return True
            node = trie[node].next[ci]
            textIndex += 1
            if textIndex >= len(text):
                return (trie[node].isLeaf(), textIndex)
            ci = letterToIndex(text[textIndex])
        else:
            return False

def createPatterns(SUF):
    pat = []
    for p in range(0, len(SUF)):
        pat.append(SUF[p:])
    return pat    

def solve (text, patterns):
    result = []
    global trie
    trie = build_trie(patterns)
    
    for t in range(len(text)):
        if PrefixMatch(text[t:], trie): result.append(t)
    return result

def overlap(PRE, SUF):
    result = []
    patterns = createPatterns(SUF)
    global trie
    trie = build_trie(patterns)
    
    for t in range(len(PRE)):
        if PrefixMatch(PRE[t:], trie): result.append(t)
    return result


PRE = "TTCGG"
SUF = "GGTT"

# =============================================================================
# PRE = "AAC"
# SUF = "ACG"
# =============================================================================

# =============================================================================
# PRE = "GTT"
# SUF = "TCG"
# =============================================================================


# =============================================================================
# PRE = "TCG"
# SUF = "GTT"
# =============================================================================

# =============================================================================
# SUF = "GGTTT"
# PRE = "TTCGG"
# =============================================================================
# =============================================================================
# PRE = "AAATTTT"
# SUF = "GCTGAAA"
# =============================================================================



ans = overlap(PRE, SUF)
print(ans)
# =============================================================================
# ans = overlap(SUF, PRE)
# print(ans)
# =============================================================================
