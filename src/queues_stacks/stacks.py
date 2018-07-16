#Stacks are LIFO
#Push items to the back and pop them off
#These work like lists

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, obj):
        self.items.append(obj)
    
    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)