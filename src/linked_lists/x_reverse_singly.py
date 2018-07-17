
class Single_Link_Node(object):
    def __init__(self,value):
        self.value = value
        self.next_node = None


def reverse(head):
    next_node = None
    curr_node = None
    prev_node = None


    while (head):
        next_node = head.next_node 
        curr_node = head

        head.next_node = prev_node 

        head = next_node
        prev_node = curr_node
    return curr_node


a = Single_Link_Node(1)
b = Single_Link_Node(2)
c = Single_Link_Node(3)
d = Single_Link_Node(4)
a.next_node = b
b.next_node = c
c.next_node = d

print(a.next_node.value)
print(b.next_node.value)
print(c.next_node.value)

reverse(a)
print('reversing')
print(d.next_node.value)
print(c.next_node.value)
print(b.next_node.value)