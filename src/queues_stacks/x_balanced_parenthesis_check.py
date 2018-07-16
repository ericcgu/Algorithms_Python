'''
Problem Statement
Given a string of opening and closing parentheses, check whether it’s balanced. 
We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. 
Assume that the string doesn’t contain any other character than these, no spaces words or numbers. 
As a reminder, balanced parentheses require every opening parenthesis 
to be closed in the reverse order opened. 
For example ‘([])’ is balanced but ‘([)]’ is not.
'''
bracket_map = {
    '{':'}',
    '[':']',
    '(':')'
}

def balance_check(s):
    stack = []

    for char in s:
        if char in bracket_map.keys():
            stack.append(bracket_map[char])
        else:
            #we know not a starter
            if len(stack) > 0 and char == stack[len(stack)-1]:
                stack.pop()
            else:
                return False
    return len(stack) == 0



print(balance_check('[[[]])]'))
