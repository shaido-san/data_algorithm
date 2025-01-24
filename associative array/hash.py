from string import ascii_letters

def hash_func(text):
    hash_num = 0
    for c in text:
        hash_num += ascii_letters.index(c)
    return hash_num

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
    
    def __str__(self):
        return "{key}:{value}".format(key=self.key, value=self.value)

class Hashtable:

    def __init__(self):
        self.size = 100
        self.data = [None] * self.size
    
    def set(self, key, value):
        hash_key = hash_func(key) % self.size
        self.data[hash_key] = Node(key, value)
    
    def get(self, key):
        hash_key = hash_func(key) % self.size
        return self.data[hash_key]
    
    def delete(self, key):
        hash_key = hash_func(key) % self.size
        self.data[hash_key] = None
    
    def __str__(self):
        result = ""
        for idx, node in enumerate(self.data):
            if node:
                result += str(idx) + ":" + str(node) + "\n"
        return result

map = Hashtable()
map.set("Tanaka", "tanaka@example.com")
map.set("Ootani", "ootani@example.com")
print(map)

mail = map.get("Tanaka")
print("mail:", mail)
