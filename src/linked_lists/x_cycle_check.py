#Return True if Linked List contains a cycle

def has_cycle(head):
    counter = set()
    
    while head is not None:
        if head in counter:
            return True
        else:
            counter.add(head)
            head = head.next

