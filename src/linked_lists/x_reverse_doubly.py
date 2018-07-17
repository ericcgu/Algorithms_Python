def reverse(head):
    curr_node = None

    while head:

        next_node = head.next
        curr_node = head
        
        head.next = head.prev
        head.prev = next_node
        
        head = next_node
    
    return curr_node
