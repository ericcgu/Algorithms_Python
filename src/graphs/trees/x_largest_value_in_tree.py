'''
You have a binary tree t. 
Your task is to find the largest value in each row of this tree. 
In a tree, a row is a set of nodes that have equal depth. 
For example, a row with depth 0 is a tree root, a row with depth 1 is 
composed of the root's children, etc.

Return an array 
'''


def largestValuesInTreeRows(t):
    seen = {} 
    depth = 1
    
    if t:
        q = [(t, depth)]
        
        while q:
            current, depth = q.pop(0)
            if depth not in seen:
                seen[depth] = current.value
            elif seen[depth] < current.value:
                seen[depth] = current.value
            depth += 1    
            if current.left:
                q.append((current.left, depth))
            if current.right:
                q.append((current.right, depth))
    return list(seen.values())

