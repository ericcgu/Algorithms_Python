#Queues are FIFO
#Push items to the top of the list, pop from the back

class Queue(object):
    def __init__(self):
        self.items = []

    def push(self, obj):
        self.items.insert(0, obj)
    
    def pop(self):
        self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)