#recursion can apply to both functions and data structures

import pprint

pp = pprint.PrettyPrinter(width=700) 

def rec_sum(n):
    if n == 0:
        return 0 
    return rec_sum(n-1) + n

