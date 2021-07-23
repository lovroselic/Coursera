# python3

#https://d3c33hcgiwev3.cloudfront.net/_4263e06c8125bf427a1ea5016af3722d_08_binary_search_trees_3_basic_ops.pdf?Expires=1576713600&Signature=CPKMg~p7MGLbWPvn-TrRL3EeKOLKEk7NVbETmgI9OqplnGIeMwOuN-sDOp93K3kzgSUhijIS3U58vg~u5f0PqzCRdm8iIGUe7gOSLPtNzJwViLdnJVh~EKNKLe2VTNPlymAYXjkxjZ6Khi8lIkFSR1UGfpochs-AjEP8x8Qk9m8_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
#https://d3c33hcgiwev3.cloudfront.net/_dcd92aaa67bc3625bc1b435b473794ba_08_binary_search_trees_4_balance.pdf?Expires=1576713600&Signature=VnpydYPEX9Yi3AER9EJtq1IHLZgRTdycXxdrCZh1x4HR4ZnuzfEbmdgwAohIuFVwCKvbpI7YBcqxLsBDwV-JT0KrGpVPFnCYdTCDtUEYoqCqh0XKxdSREmILi0fKXIy6VLhaoTtdzIX4vfuCVktm4xAbgIPKbNL1T~XZvhvRj~s_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
#https://d3c33hcgiwev3.cloudfront.net/_bd63e90c34461825e4308eada52801d1_05_3_trees.pdf?Expires=1576713600&Signature=DVJ6~WePPdf7aiqVLvCAWFa89Mw4KEiaAdPzziI0zRp7PtPuQvxnJt7y5Ee7dDL8aOvMU5lVDNpmWk45~xXTC0zVZvHgDVjBeqzPj6rxxanZPHddJ0mFpjfkxp85ngA1L1niLfRLk3JFPbJRxDtNxNxfAtJkDL6iSEOt-YSlRrM_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
#https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

#
#test = open("tests\\21", "r")
#print(test.read())

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    #self.n = int(test.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      #[a, b, c] = map(int, sys.stdin.readline().split())
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

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
