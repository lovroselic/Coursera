#Uses python3
import sys

NA = -1
#DEBUG = False
DEBUG = True
if DEBUG: test = open("tests\\3", "r")

class Node:
	def __init__ (self):
		self.next = [NA] * 4


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
        
def letterToIndex(char):
    if char == "A": return 0
    if char == "C": return 1
    if char == "G": return 2
    if char == "T": return 3
    return None

def build_trie(patterns):
    tree = []
    for pat in patterns:
        if DEBUG: print(pat)
        node = 0
        for c in pat:
            #if node does not exist, create one
            if len(tree) < (node + 1):
                tree.append(Node())
            i = letterToIndex(c)
            if tree[node].next[i] != -1:
                node = tree[node].next[i]
            else:
                #point po next leaf
                tree[node].next[i] = len(tree)
                node = len(tree)
                #
                if len(tree) < (node + 1):
                    tree.append(Node())
    return tree


if __name__ == '__main__':
    #patterns = sys.stdin.read().split()[1:]
    patterns = test.read().split()[1:]
    if DEBUG: print(patterns)
    tree = build_trie(patterns)
    print(tree)
# =============================================================================
#     for node in tree:
#         for c in tree[node]:
#             print("{}->{}:{}".format(node, tree[node][c], c))
# =============================================================================
