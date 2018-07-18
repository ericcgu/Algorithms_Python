
class BinaryTree(object):
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def _is_parent(node):
        return bool(node.left or node.right)

    def _is_interior(self, node):
        return (not node == self.root) and self.is_parent(node)

    def _is_leaf(self, node):
        return (not node == self.root) and not self.is_interior(node)
    
    


    def insert_left(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            new = BinaryTree(node)
            new.left = self.left
            self.left = new
    
    def insert_right(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            new = BinaryTree(node)
            new.right = self.right
            self.right = new

    def depth(self, node):
        if not node:
            return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1

    def is_balanced(self, node):
        if not node:
            return True
        
        left_height = self.depth(node.left)
        right_height = self.depth(node.right)
        
        if (abs(right_height - left_height) <= 1
               and self.is_balanced(node.left)
               and self.is_balanced(node.right)):
            return True
        return False    
   

tree = BinaryTree('a')
tree.insert_left('b')
tree.insert_left('e')
tree.insert_left('f')
tree.insert_left('g')
tree.insert_right('c')


def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.left)
        preorder(tree.right)

def postorder(tree):
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.key)

def num_nodes(tree):
    if tree is None:
        return 0
    if tree:
        return 1 + num_nodes(tree.left) + num_nodes(tree.right)

print(tree.is_balanced(tree))
print(num_nodes(tree))

