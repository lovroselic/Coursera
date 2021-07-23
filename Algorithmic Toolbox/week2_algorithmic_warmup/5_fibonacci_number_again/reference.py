# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:12:57 2019

@author: SELICLO1
"""

#python3
def pisano_length(m):
    i=2
    while(fib(i)%m!=0):
        i+=1
    if(fib(i+1)%m!=1):
        while(fib(i+1)%m!=1):
            i+=i
    print("The pisano length for mod {} is: {}".format(m,i))
    return(i)
def fib(n):
    a,b=0,1
    if(n==0 or n==1):
        return n
    else:
        for i in range(2,n+1):
            b,a=a+b,b
    return(b)
#we want to calculate fib(n)%m for big numbers
#n,m=map(int,input().split())
n = 239
m = 1000
remainder=n%pisano_length(m)
print(fib(remainder)%m)