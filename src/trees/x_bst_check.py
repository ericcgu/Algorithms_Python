tree_vals = []

def inorder(tree):
    if tree:
        inorder(tree.left)
        tree_vals.append(tree.key)
        inorder(tree.right)
    
def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)