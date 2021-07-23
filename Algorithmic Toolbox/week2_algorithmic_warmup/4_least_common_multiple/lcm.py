# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        #print(l)
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm(a,b):
    res = (a * b) / gcd(a,b)
    return int(res)

def gcd(a,b):
    if b == 0:
        return a
    a_prime = a % b
    return gcd(b, a_prime)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())

    #print(lcm_naive(a, b))
    #print(gcd(a,b))
    print(lcm(a, b))

