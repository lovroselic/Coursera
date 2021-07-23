# Uses python3

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

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

n = int(input())
print(fast_calc_fib(n))
