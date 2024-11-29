class Node:
    def __init__(self, x): self.val, self.left, self.right = x, None, None

def insert(root, x):
    if not root: return Node(x)
    if x < root.val: root.left = insert(root.left, x)
    else: root.right = insert(root.right, x)
    return root

def inorder(root):
    if root: inorder(root.left); print(root.val, end=" "); inorder(root.right)

root = None
for val in [5, 3, 8, 6, 2]: root = insert(root, val)
inorder(root)
