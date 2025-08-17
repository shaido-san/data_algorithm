import random

class Node:
    def __init__(self, key, priority=None):
        self.key = key
        self.priority = priority if priority is not None else random.random()
        self.left = None
        self.right = None

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
        if root.left.priority < root.priority:  # ヒープ条件違反なら右回転
            root = rotate_right(root)
    else:
        root.right = insert(root.right, key)
        if root.right.priority < root.priority:  # ヒープ条件違反なら左回転
            root = rotate_left(root)
    return root

def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return True
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

def inorder(root):
    if root:
        yield from inorder(root.left)
        yield root.key
        yield from inorder(root.right)

# --- 使い方 ---
root = None
for key in [5, 3, 8, 1, 4, 7, 9]:
    root = insert(root, key)

print("Inorder traversal:", list(inorder(root)))
print("Search 4:", search(root, 4))
print("Search 6:", search(root, 6))