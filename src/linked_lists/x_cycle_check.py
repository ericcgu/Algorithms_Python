#Return True if Linked List contains a cycle

def cycle_check(node):
    counter = set()
    
    while node:
        if node in counter:
            return True
        else:
            counter.add(node)
            node = node.nextnode
    return False

def reverse(node):
    current = head
    previous = None
    next = None