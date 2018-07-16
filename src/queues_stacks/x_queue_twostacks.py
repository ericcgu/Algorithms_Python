#implement a queue using two stacks

class Queue2Stacks(object):
    
    def __init__(self):
        # Two Stacks
        self.instack = []
        self.outstack = []
     
    def enqueue(self,element):
        
        # Add an enqueue with the "IN" stack
        self.instack.append(element)
    
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

test = Queue2Stacks()

test.enqueue(1)
test.enqueue(2)
test.enqueue(3)

print(test.dequeue())
print(test.dequeue())
print(test.dequeue())