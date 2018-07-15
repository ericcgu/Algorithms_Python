#Stacks are LIFO
#Push Stack on the bottom of Stack

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