class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
     tortoise = hare = head
     while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            return True
     return False

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
d.next = b

print(has_cycle(a))