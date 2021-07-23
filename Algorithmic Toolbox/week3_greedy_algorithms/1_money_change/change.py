# Uses python3
import sys

def get_change(m):
    #write your code here
    ten = int(m / 10)
    rem = m % 10
    five = int(rem / 5)
    rem = rem % 5
    return ten + five + rem

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = 35
    print(get_change(m))
