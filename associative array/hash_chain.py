class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.value = value
        self.next = next
    
    def __str__(self):
        if self.next:
            return str(self.value) + " - " + str(self.next)
        else:
            return str(self.value)
    
node1 = Node("key1", "data1")
node2 = Node("key2", "data2")
node3 = Node("key3", "data3")
node1.next = node2
node2.next = node3
print(node1)