#Doubly Linked List
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

