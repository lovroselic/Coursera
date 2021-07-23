# Uses python3
import sys

def optimal_summands(n):
    #print(n)
    summands = []
    #write your code here
    #=========
    for i in range(1, n + 1):
        #print("++++++++++")
        #print(i, n, n - 1)
        if n - 1 < i * 2:
            #print("appending n", n)
            summands.append(n)
            break
        else:
            #print("appending i", i)
            summands.append(i)
            n -= i
            i += 1    
    #=========
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    #n = 62
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
