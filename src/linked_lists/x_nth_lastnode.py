
class Single_Link_Node(object):
    def __init__(self,value):
        self.value = value
        self.next_node = None

a = Single_Link_Node(1)
b = Single_Link_Node(2)
c = Single_Link_Node(3)
d = Single_Link_Node(4)
e = Single_Link_Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

def nth_to_last_node(n, head):
    linked_list = []
    while head:
        linked_list.append(head)
        head = head.next_node
    return linked_list[-2].value

print(nth_to_last_node(2, a))
