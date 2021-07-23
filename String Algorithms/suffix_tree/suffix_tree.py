# python3

#https://www.geeksforgeeks.org/generalized-suffix-tree-1/
import sys

NA = -1

#DEBUG = False
DEBUG = True
if DEBUG: test = open("sample_tests\\sample3", "r")

class Node:
    def __init__ (self):
        self.next = [NA] * 5
        #self.children = [NA] * 5
        #self.patternEnd = [False] * 5
        #self.symbol = []
        self.leaf = False
        self.single = True
        self.pos = None
        self.len = None
        
# =============================================================================
#     def isLeaf(self):
#         return self.next[0] == -1 and self.next[1] == -1 and self.next[2] == -1 and self.next[3] == -1 and self.next[4] == -1
#     
# =============================================================================
# =============================================================================
#     def terminal(self):
#         return self.next[0] == 0
# =============================================================================
        
def letterToIndex(char):
    if char == "A": return 1
    if char == "C": return 2
    if char == "G": return 3
    if char == "T": return 4
    if char == "$": return 0
    return None


# =============================================================================
# def suffix_trie(text):
#     tree = []
#     tree.append(Node())
#     for t in range(len(text)):
#         pat = text[t:]
#         if DEBUG: print(pat, t)
#         node = 0
#         for ci in range(len(pat)):
#             c = pat[ci]
#             if DEBUG: print(c, t + ci)                 
#             i = letterToIndex(c)
#             if ci == len(pat) - 1:
#                 tree[node].patternEnd[i] = True
#             if tree[node].next[i] != -1:
#                 node = tree[node].next[i]
#                 #tree[node].pos[i] = t
#             else:
#                 tree[node].pos[i] = (t + ci)
#                 tree[node].len[i] = 1
#                 tree[node].next[i] = len(tree)
#                 node = len(tree)
#                 if len(tree) < (node + 1):
#                     tree.append(Node())
#     return tree
# =============================================================================

def suffix_trie(text):
    tree = []
    tree.append(Node())
    for t in range(len(text)):
        pat = text[t:]
        if DEBUG: print(pat, t)
        node = 0
        for ci in range(len(pat)):
            c = pat[ci]
            if DEBUG: print(c, t + ci)                 
            i = letterToIndex(c)
            if ci == len(pat) - 1:
                tree[node].patternEnd[i] = True
            if tree[node].next[i] != -1:
                node = tree[node].next[i]
                #tree[node].pos[i] = t
            else:
                tree[node].pos[i] = (t + ci)
                tree[node].len[i] = 1
                tree[node].next[i] = len(tree)
                node = len(tree)
                if len(tree) < (node + 1):
                    tree.append(Node())
    return tree

def build_suffix_tree(text):
      """
      Build a suffix tree of the string text and return a list
      with all of the labels of its edges (the corresponding 
      substrings of the text) in any order.
      """
      global trie
      trie = suffix_trie(text)
      result = []
      # Implement this function yourself
      return result


if __name__ == '__main__':
    if DEBUG: 
        text = test.readline ().strip ()
    else:
        text = sys.stdin.readline ().strip ()
        #text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    #if DEBUG: print(text)
    print("\n".join(result))