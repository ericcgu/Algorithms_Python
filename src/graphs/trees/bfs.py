#Breadth First Search
#Key is the Queue
# 
# A BFS on a binary tree generally requires more memory than a DFS.

class Tree(object):
   def __init__(self, x):
     self.value = x
     self.left = None
     self.right = None

def traverseTree(t):
    seen = []
    if t:
        q = [t] #queue
        while q:
            current = q.pop(0)
            seen.append(current.value) #key action
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
    return seen