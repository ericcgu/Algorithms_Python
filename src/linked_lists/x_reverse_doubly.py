def reverse(head):
    curr = None

    while head:

        nxt = head.next
        curr = head
        
        head.next = head.prev
        head.prev = nxt
        
        head = nxt
    
    return curr