#Uses python3
import sys

#DEBUG = False
DEBUG = True
if DEBUG: test = open("tests\\3", "r")


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    #tree = {0:{'A':1}, 1:{'C': 4, 'G': 3, 'T':2}}
    count = 0
    for pat in patterns:
        node = 0
        for c in pat:
            if not(node in tree):
                tree[node] = {}
                
            if c in tree[node]:
                node = tree[node][c]
            else:
                count += 1
                tree[node][c] = count
                node = count                  
    return tree


if __name__ == '__main__':
    #patterns = sys.stdin.read().split()[1:]
    patterns = test.read().split()[1:]
    if DEBUG: print(patterns)
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
