class ListNode(object):
   def __init__(self, x):
     self.value = x
     self.next = None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

l = [a,b,c]



def removeKFromList(l, k):
    linked_list = []
    while l:
        if l != k:
                linked_list.append(l)
        l = l.next
    return linked_list

print(removeKFromList(l, b))