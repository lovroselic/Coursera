#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__aux = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__aux) == 0:
            self.__aux.append(a)
        else:
            self.__aux.append(max(a, self.__aux[-1]))

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__aux.pop()

    def Max(self):
        assert(len(self.__aux))
        return self.__aux[-1]


# =============================================================================
# inp = '''
# 6
# push 7
# push 1
# push 7
# max
# pop
# max
# '''
# I = inp.splitlines()
# 
# stack = StackWithMax()
# num_queries = int(I[1])
# queries = I[2:]
# for q in range(len(queries)):
#     #print(queries[q])
#     query = queries[q].split()
#     if query[0] == "push":
#         stack.Push(int(query[1]))
#     elif query[0] == "pop":
#         stack.Pop()
#     elif query[0] == "max":
#         print(stack.Max())
#     else:
#         assert(0)
# =============================================================================


stack = StackWithMax()
num_queries = int(sys.stdin.readline())
for _ in range(num_queries):
    query = sys.stdin.readline().split()
    if query[0] == "push":
        stack.Push(int(query[1]))
    elif query[0] == "pop":
        stack.Pop()
    elif query[0] == "max":
        print(stack.Max())
    else:
        assert(0)
