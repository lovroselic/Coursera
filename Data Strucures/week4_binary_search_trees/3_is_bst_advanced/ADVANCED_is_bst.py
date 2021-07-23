#!/usr/bin/python3

import sys, threading
#import math

#test = open("tests\\4", "r")

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Tree:
  def read(self):
    self.n = int(sys.stdin.readline())
    #self.n = int(test.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      #[a, b, c] = map(int, test.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def inOrder(root):
        if (root == -1): return
        inOrder(self.left[root])
        self.result.append(self.key[root])
        inOrder(self.right[root])
    
    inOrder(0)
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def preOrder(root):
        if (root == -1): return
        self.result.append(self.key[root])
        preOrder(self.left[root])
        preOrder(self.right[root])
        
    preOrder(0)            
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def postOrder(root):
        if (root == -1): return
        postOrder(self.left[root])
        postOrder(self.right[root])
        self.result.append(self.key[root])
     
    postOrder(0)           
    return self.result
  
  def find(self, root, key):
      #print(".....find", root, key)
      if (root == -1): return False
      if (self.key[root] == key): return True
      left = self.find(self.left[root], key)
      if (left): return True
      right = self.find(self.right[root], key)
      return right

    
def isBST(tree, root):
    global prev
    global stored, index
    #global first
    if (root != -1):
        if (isBST(tree, tree.left[root]) == False):
            return False
        
        
# =============================================================================
#         try:
#             print("key", stored, "index", index)
#             print("DEBUG", "root", tree.key[root], "second", tree.key[prev])
#         except:
#             pass
# =============================================================================
            
        if (prev is not None): 
            if (tree.key[root] < tree.key[prev]):
                return False
            elif (tree.key[root] == tree.key[prev]):
                #print(".... is EQ", stored[-1], "idx", index[-1])
                #find if this is in RST of prev
                RC = tree.find(tree.right[index[-1]], stored[-1])
                #print("RC", RC)
                if (not RC): return False
        
                
        stored.append(tree.key[root])
        index.append(root)
        prev = root
        return isBST(tree, tree.right[root])   
    return True
    

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if (tree.n == 0): return True
  global prev 
  global stored, index
  stored = []
  index = []
  prev = None
  return isBST(tree, 0)


def main():
  #nodes = int(sys.stdin.readline().strip())
  #nodes = int(test.readline().strip())

  tree = Tree()
  tree.read()
  #print("sorted:"," ".join(str(x) for x in tree.inOrder()))
# =============================================================================
#   for i in range(nodes):
#     #tree.append(list(map(int, sys.stdin.readline().strip().split())))
#     tree.append(list(map(int, test.readline().strip().split())))
# =============================================================================
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
