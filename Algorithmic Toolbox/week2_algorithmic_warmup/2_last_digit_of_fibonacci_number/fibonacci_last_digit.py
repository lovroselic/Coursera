# Uses python3
import sys
def fast_calc_fib(n):
    if n <= 1:
        return n
    fib= [None]* (n + 1)
    fib[0] = 0
    fib[1] = 1
    for q in range(2,n+1):
        fib[q] = (fib[q-1] + fib[q-2]) % 10
    #print(fib)    
    return fib[n]

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fast_calc_fib(n))
