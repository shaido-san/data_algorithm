import random

class SkipNode:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None]*level

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = SkipNode(-1, max_level)

    def random_level(self):
        level = 1
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        update = [None] * self.max_level
        curr = self.head

        for i in reversed(range(self.max_level)):
            while curr.forward[i] and curr.forward[i].value < value:
                curr = curr.forward[i]
            update[i] = curr

        level = self.random_level()
        new_node = SkipNode(value, level)
        for i in range(level):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, value):
        curr = self.head
        for i in reversed(range(self.max_level)):
            while curr.forward[i] and curr.forward[i].value < value:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr and curr.value == value

sl = SkipList(4)
for v in [3, 6, 7, 9, 12, 19, 21]:
    sl.insert(v)

print("Found 19:", sl.search(19))
print("Found 5:", sl.search(5))