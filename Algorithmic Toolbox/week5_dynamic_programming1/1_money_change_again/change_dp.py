# Uses python3
import sys
import math

def get_change(money):
    #write your code here
    minCoins = [0] + [math.inf]*money
    for m in range(1, money+1):
        for c in coins:
            if m >= c:
                numCoins = minCoins[m-c]+1
                if numCoins < minCoins[m]:
                    minCoins[m] = numCoins  
    return minCoins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    coins = [1, 3, 4]
    print(get_change(m))
