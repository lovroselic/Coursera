# Uses python3
import sys

def fast_calc_fib(n):
    if n <= 1:
        return n
    fib= [None]* (n + 1)
    fib[0] = 0
    fib[1] = 1
    for q in range(2,n+1):
        fib[q] = fib[q-1] + fib[q-2]
    #print(fib)    
    return fib[n]

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def piLength(m):
    F1 = 0
    F2 = 1
    F = F1 + F2
    for i in range(0, m**2):
        F = (F1 + F2) % m
        F1 = F2
        F2 = F
        if F1 == 0 and F2 == 1:
            return i+1
    
    return None

def get_fibonacci_huge_mod(n,m):
    if n < 2:
        return n
    remain = n % piLength(m)
    return fast_calc_fib(remain) % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_mod(n, m))
