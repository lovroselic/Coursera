# Uses python3
import sys
class item:
    def __init__(self, stock, price):
        self.stock = stock
        self.price = price
        
def printList(lst):
    print("===============================")
    index = 0
    for it in lst:
        #print(it)
        print(index)
        props = filter(lambda a: not a.startswith('__'), dir(it))
        #print(props)
        for prop in props:
            print(prop, getattr(it, prop))
        index += 1
        print("===============================")
        
def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    #print(capacity, weights, values)
    vpw = []
    for i in range(0, len(weights)):
        vpw.append(item(weights[i], values[i] / weights[i]))

    #sort by price
    vpw.sort(key=lambda x: x.price, reverse=True)
    #printList(vpw)
    
    index = 0
    iteration = 1
    N = len(vpw)
    while capacity > 0 and index < N:
        #print("round", iteration, capacity)
        #printList(vpw)
        grab = min(capacity, vpw[index].stock)
        #print("grab", grab)
        capacity -=grab
        vpw[index].stock -= grab
        value += grab * vpw[index].price
        index += 1
        iteration += 1
        
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #input = "3 50 60 20 100 50 120 30" #180 
    #input = "1 10 500 30"
    #input = "1 1000 500 30"
    #data = list(map(int, input.split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
