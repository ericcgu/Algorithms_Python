
class BinaryTree(object):
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
    
    def insert_left(self, node):
        if self.leftChild == None:
            self.leftChild = BinaryTree(node)
        else:
            newNode = BinaryTree(node)
            newNode.leftChild = self.leftChild
            self.leftChild = newNode
    
    def insert_right(self, node):
        if self.rightChild == None:
            self.rightChild = BinaryTree(node)
        else:
            newNode = BinaryTree(node)
            newNode.rightChild = self.rightChild
            self.rightChild = newNode

r = BinaryTree('a')
r.insert_left('b')
print(r.leftChild.key)
