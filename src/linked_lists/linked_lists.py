#can expand without having pre-determined fixed size
#constant time insert and deletion
#con O(k) time to access the element

#Single Linked List
class Single_Link_Node(object):
    def __init__(self,value):
        self.value = value
        self.next_node = None

a = Single_Link_Node(1)
b = Single_Link_Node(2)
c = Single_Link_Node(3)

a.next_node = b
b.next_node = c

print(a.next_node.value)
print(b.next_node.value)

#Single Linked List
class Double_Link_Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

a = Double_Link_Node(1)
b = Double_Link_Node(2)
c = Double_Link_Node(3)

a.next_node = b
b.prev_node = a
b.next_node = c
c.prev_node = b


