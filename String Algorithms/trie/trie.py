#Uses python3
import sys

test = open("tests\\3", "r")
#DEBUG = True
DEBUG = False

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
        #if DEBUG: print(pat)
        node = 0
        for c in pat:
            #if DEBUG: print("->", c, " node ", node)
            if not(node in tree):
                #if DEBUG: print("NEW node")
                tree[node] = {}
                count += 1
                tree[node][c] = count
                #if DEBUG: print(tree[node])
                node = count
                continue
                
            if c in tree[node]:
                #next edge
                #if DEBUG: print(c, " in ", tree[node])
                node = tree[node][c]
                #if DEBUG: print("next node", node)
            else:
                #if DEBUG: print(c, " NOT in ", tree[node], node)
                #if DEBUG: print("NEW node")
                count += 1
                tree[node][c] = count
                #if DEBUG: print(tree[node])
                node = count                  
    #
    return tree


if __name__ == '__main__':
    #patterns = sys.stdin.read().split()[1:]
    patterns = test.read().split()[1:]
    if DEBUG: print(patterns)
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
