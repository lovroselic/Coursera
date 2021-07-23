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
def fib2(n):
    f = fast_calc_fib(n)
    return f**2

#n = int(input())
for n in range(0,10 + 1):
    print(n, fast_calc_fib(n), fib2(n), fast_calc_fib(n) % 10, fib2(n) % 10)
