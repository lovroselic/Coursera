# Uses python3
import sys
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

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum(from_, to):
    pi = piLength(10)
    frSum = get_fibonacci_huge_mod(from_ + 1, 10, pi) - 1 
    toSum = get_fibonacci_huge_mod(to + 2, 10, pi) - 1 
    sum = toSum - frSum
    #print(toSum, frSum, sum)
    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    #input = "3 7"
    #input = "10 10"
    #input = "10 200"
    from_, to = map(int, input.split())
    #print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum(from_, to))