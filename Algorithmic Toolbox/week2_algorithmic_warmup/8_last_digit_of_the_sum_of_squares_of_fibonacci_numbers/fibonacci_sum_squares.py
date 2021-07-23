# Uses python3
from sys import stdin
#FIB libs
def fast_calc_fib(n):
    if n <= 1:
        return n
    return get_fib_list(n)[n]

def get_fib_list(n):
    fib= [None] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    for q in range(2,n+1):
        fib[q] = fib[q-1] + fib[q-2]
    return fib

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

def get_fibonacci_huge_mod_pi(n,m):
    if n < 2:
        return n
    remain = n % piLength(m)
    return fast_calc_fib(remain) % m

def get_fibonacci_huge_mod(n,m, pi):
    if n < 2:
        return n
    remain = n % pi
    return fast_calc_fib(remain) % m

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fib_sum_huge_slow(n):
    if n <= 1:
        return n
    
    pi = piLength(10)
    sum = 1
    for i in range(2, n + 1):
        sum += get_fibonacci_huge_mod(i, 10, pi)        
    return sum % 10

def fib_sum_huge_fast(n):
    if n <= 1:
        return n    
    pi = piLength(10)
    sum = get_fibonacci_huge_mod(n + 2, 10, pi) - 1 
    return sum % 10
#

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10
def fibonacci_sum_squares(n):
    pi = piLength(10)
    Fn = get_fibonacci_huge_mod(n, 10, pi) 
    Fn1 = get_fibonacci_huge_mod(n+1, 10, pi) 
    res = (Fn * Fn1) % 10
    return res

if __name__ == '__main__':
    n = int(stdin.read())
    #n = 1234567890
    #print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares(n))
