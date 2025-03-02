class Node:
    def __init__(self, key, value, is_left=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.is_left = is_left
    
    def __str__(self):
        return str(self.key) + ":" + str(self.value)
    

class MyBsTree:
    def __init__(self):
        self.root = None