
class Single_Link_Node(object):
    def __init__(self,value):
        self.value = value
        self.next_node = None


def reverse(head):
    current_node = head
    previous_node = None
    next_node = None

    while (current_node):
        next_node = current_node.next_node #SAVING B
        current_node.next_node = previous_node 

        previous_node = current_node
        current_node = next_node


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