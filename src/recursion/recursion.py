#recursion can apply to both functions and data structures
import sys
import pprint
sys.setrecursionlimit(1500)
pp = pprint.PrettyPrinter(width=700) 

def number_sum(n):
    if n == 0:
        return 0 
    return n + number_sum(n-1)

def digit_sum(n):
    # Base case
    if n < 10:
        return n
    
    # Recursion
    else:
        return n % 10 + digit_sum(n // 10)
        

