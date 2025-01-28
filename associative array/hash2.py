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
        while hash_key < self.size:
            node = self.data[hash_key]
            if node is None or node.key == '-':
                self.data[hash_key] = Node(key, value)
                return
            
            # ハッシュの再計算
            hash_key += 1
        
        print("空きが見つかりませんでした")
    
    def get(self, key):
        hash_key = hash_func(key) % self.size
        while hash_key < self.size:
            node = self.data[hash_key]
            if node is None:
                print("データがみつかりませんでした")
                return
            
            elif node.key == key:
                return node.value
            
            # ハッシュ値の再計算
            hash_key += 1
        
        print("データが見つかりませんでした")
    
    def delete(self, key,):
        hash_key = hash_func(key) % self.size
        while hash_key < self.size:
            node = self.data[hash_key]
            if node is None:
                print("データが見つかりませんでした")
                return
            
            elif node.key == key:
                self.data[hash_key] = Node('-', None)
                return
            
            # ハッシュ値の再計算
            hash_key += 1
    
    def __str__(self):
        result = ""
        for idx, node in enumerate(self.data):
            if node:
                result += str(idx) + ":" + str(node) + "\n"
        return result

map = Hashtable()
map.set("suzuki", "suzuki@example.com")
# map.set("ootani", "ootani@example.com")
map.set("nakata", "nakata@example.com")
map.set("tanaka", "tanaka@example.com")
# map.set("toudou", "toudou@example.com")

print(map)
map.delete("nakata")
print(map)
val = map.get("tanaka")
print(val)
map.set("kanata", "kanata@example.com")
print(map)
# print(map.get("toudou"))
# print(map.get("ootani"))
# print(map.get("tanaka"))
# print(map.get("kanata"))
# print(map.get("nakata"))
# mail = map.get("Tanaka")
# print("mail:", mail)
