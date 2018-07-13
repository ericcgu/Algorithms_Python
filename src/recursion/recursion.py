#recursion can apply to both functions and data structures
import sys
import functools



def number_sum(n):
    if n == 0:
        return 0 
    return n + number_sum(n-1)

def digit_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + digit_sum(n // 10)

@functools.lru_cache(maxsize=None)
def reverse_string(str):
    if len(str) == 0:
        return str
    return reverse_string(str[1:]) + str[0]     

@functools.lru_cache(maxsize=None)
def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a    

@functools.lru_cache(maxsize=None)
def fib_rec(n):
    if n == 0 or n == 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

