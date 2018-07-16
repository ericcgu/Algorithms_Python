#Deque: add and remove from top and bottom

class Queue(object):
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0,item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        self.items.pop(0)

    def remove_rear(self):
        self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)